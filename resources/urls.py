
from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt import views as jwt_views
from .libs.auth import UserLoginViewJWT
urlpatterns = [
    # JWT Token
    url(r'^token/?$', UserLoginViewJWT.as_view(), name='api_token_obtain'),
    url(r'^token/refresh/?$', jwt_views.RefreshJSONWebToken.as_view(), name='api_token_refresh'),
    
   url('^songs/', ListSongsView.as_view(), name="songs-all"),
   #url('songs/', ListSongs, name="songs-all"),
   url('^artists/', ListArtistsView.as_view(), name="artists-all"),
   url('^albums/', ListAlbumsView.as_view(), name="albums-all"),
   url('^playlists/', ListPLsView.as_view(), name="PlayLists"),
   
   url('^userFav/', ListUserFavoritesView.as_view(), name="UserFavorites"),
   url('^saveFavorite/', saveFavorite, name="saveFavorite"),
   
   
   url('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
