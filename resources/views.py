from django.shortcuts import render
# Create your views here.
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core import serializers
from django.forms.models import model_to_dict
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.db.models import Q
from django.http import JsonResponse
class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #queryset = Songs.objects.all()
    model     = Song
    serializer_class = SongsSerializer

    def get_queryset(self):
        args = {}
        art_id = int(self.request.GET.get("artist",False))
        alb_id = int(self.request.GET.get("album",False))
        limit  = int(self.request.GET.get("limit",8))
        
        if art_id>0:
            args["artists"] = art_id
        if alb_id>0:
            args["album"] = alb_id
        
        songs = Song.objects.filter(**args)
        if limit>0:
            songs = songs[:limit]
        
        return songs
    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(ListSongsView, self).list(request, *args, **kwargs) 
        # customize the response data
        songs_list = []
        for row in response.data:
            response.data
            song_ = dict(row)
            artcs= Artist.objects.filter(id__in=song_["artists"])
            #row["artists"] = serializers.serialize("json" , artcs)
            row["artists"] =  [ model_to_dict(x) for x in artcs ]
         

        # return response with this custom representation
        return response 

    
class ListArtistsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #permission_classes = (IsAuthenticated,)
    queryset = Artist.objects.all()
    serializer_class = ArtistsSerializer
    
    
    
class ListAlbumsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #permission_classes = (IsAuthenticated,)
    model = Album
    serializer_class = AlbumsSerializer
    
    def get_queryset(self):
        args = {}
        art_id = int(self.request.GET.get("artist",False))
        limit  = int(self.request.GET.get("limit",8))
        if art_id>0:
            args["artists"] = art_id
        albums = Album.objects.filter(**args)
        if limit>0:
            albums = albums[:limit]
        return albums
    
    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(ListAlbumsView, self).list(request, *args, **kwargs) 
        # customize the response data
        songs_list = []
        for row in response.data:
            response.data
            album_ = dict(row)
            artcs= Artist.objects.filter(id__in=album_["artists"])
            #row["artists"] = serializers.serialize("json" , artcs)
            row["artists"] =  [ model_to_dict(x) for x in artcs ]
         
        return response 
    
    
class ListPLsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #permission_classes = (IsAuthenticated,)
    model = PlayList
    serializer_class = PlayListsSerializer
    
    def get_queryset(self):
        print(self.request.user.id)
        args = {}
        user_id = int(self.request.GET.get("user_id",False))
        limit  = int(self.request.GET.get("limit",8))
        if user_id>0:
            args["created_by"] = user_id
            
        PLs = PlayList.objects.filter(Q(created_by=self.request.user) | Q(is_private=False) )
        if limit>0:
            PLs = PLs[:limit]
        return PLs
    
    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(ListPLsView, self).list(request, *args, **kwargs) 
        allowed_cols = ("id","img_link","link_mp3","title")
        for row in response.data:
            response.data
            pl_ = dict(row)
            songs = Song.objects.filter(id__in=pl_["songs"]).only(*allowed_cols)
            row["songs"] =  [ {k:v for k,v in model_to_dict(x).items() if k in allowed_cols} for x in songs ]
            
            print(row["songs"])
         
        return response 

class ListUserFavoritesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    #permission_classes = (IsAuthenticated,)
    model = UserFavorites
    serializer_class = UserFavoritesSerializer
    def saveFave(self):
        id   = self.request.GET.get("id",False)
        type = self.request.GET.get("type",False)
        action = self.request.GET.get("action",False)
        if not id or not type :
            return True
        
        try:
            fav = UserFavorites.objects.get(user=self.request.user)
            if action == "add":
                fav.songs.add(Song.objects.get(id=id))
            else :
                fav.songs.remove(Song.objects.get(id=id))
            fav.save()
        except:
            pass
        
        return True
    def get_queryset(self):
        self.saveFave()
        args = {}
        fav_type = self.request.GET.get("type",False)
        limit  = int(self.request.GET.get("limit",8))
            
        PLs = UserFavorites.objects.filter(user=self.request.user )
        if limit>0:
            PLs = PLs[:limit]
        return PLs
    
    def list(self, request, *args, **kwargs):
        # call the original 'list' to get the original response
        response = super(ListUserFavoritesView, self).list(request, *args, **kwargs) 
        
        fav_type = self.request.GET.get("type",False)
        only_ids = self.request.GET.get("only_ids",False)
        allowed_cols = ("id",only_ids) if only_ids and only_ids!="" else ("id","songs","albums","artists","playlists")
        
        song_allowed_col = ("id","img_link","link_mp3","title")
        artist_allowed_col = ("id","img_link","first_name","last_name")
        playlists_allowed_col = ("id","img_link","title")
        for row in response.data:
            response.data
            fav = dict(row)
            if only_ids:
                continue
            if fav_type == "songs" or not fav_type or fav_type=="":
                songs     = Song.objects.filter(id__in=fav["songs"]).only(*song_allowed_col)
                row["songs"] = [ {k:v for k,v in model_to_dict(x).items() if k in song_allowed_col} for x in songs ]
            if fav_type == "albums" or not fav_type or fav_type=="":
                albums    = Album.objects.filter(id__in=fav["albums"])
                row["albums"] = [ {k:v for k,v in model_to_dict(x).items()} for x in albums ]

                for alb in row["albums"]:
                    alb["artists"] = [ {k:v for k,v in model_to_dict(x).items() if k in artist_allowed_col } for x in alb["artists"] ]
                    
                    
            if fav_type == "artists" or not fav_type or fav_type=="":
                artists   = Artist.objects.filter(id__in=fav["artists"])
                row["artists"] = [ {k:v for k,v in model_to_dict(x).items()} for x in artists ]
            if fav_type == "playlists" or not fav_type or fav_type=="":
                playlists = PlayList.objects.filter(id__in=fav["playlists"])
                row["playlists"] = [ {k:v for k,v in model_to_dict(x).items()} for x in playlists ]
                
                for pl in row["playlists"]:
                    pl["songs"] = [ {k:v for k,v in model_to_dict(x).items() if k in song_allowed_col } for x in pl["songs"] ]
        return response 
    
def saveFavorite(request):
    output = {"success":False,"msg":"","errors":None}
    print(request.user)
    userFav = UserFavorites(user=request.user)
    print(request.user)
    
    return JsonResponse(output)