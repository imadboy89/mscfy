from rest_framework import serializers
from .models import *


class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ("id","title","artists", "link_mp3", "img_link")

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ("id","full_name","img_link","country")



class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id","title","date_release","artists","img_link")
        
class PlayListsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayList
        fields = ("id","title","created_by","songs","img_link")
        
class UserFavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFavorites
        fields = ("id","songs","artists","albums","playlists")