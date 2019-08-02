from django.db import models
from django.contrib.auth.models import User

from django.db import models

class Artist(models.Model):
    full_name    = models.CharField(max_length=30)
    neck_name     = models.CharField(max_length=30,blank=True, null=True)
    country       = models.CharField(max_length=30)
    img_link      = models.CharField(max_length=250, default="https://www.sccpre.cat/mypng/full/170-1704218_singer-svg-png-icon-free-download-pop-singer.png")
    email         = models.EmailField(blank=True, null=True )
    date_addded   = models.DateTimeField(verbose_name="added to platform", blank=True, null=True,auto_now_add=True)
    date_updated  = models.DateTimeField(verbose_name="added to platform", blank=True, null=True, auto_now=True)
    def __str__(self):
        return "%s " % (self.full_name)
    class Meta:
        db_table = 'Artists'

class Album(models.Model):

    title         = models.CharField(max_length=255, null=False)
    img_link      = models.CharField(max_length=250, default="https://image.flaticon.com/icons/png/512/26/26358.png")
    date_release  = models.CharField(max_length=4, verbose_name="date released ", blank=True, null=True)
    date_addded   = models.DateTimeField(verbose_name="added to platform", blank=True, null=True,auto_now_add=True)
    date_updated  = models.DateTimeField(verbose_name="added to platform", blank=True, null=True, auto_now=True)
    artists       = models.ManyToManyField(Artist)
    def __str__(self):
        return "{} ".format(self.title) 
    class Meta:
        db_table = 'Albums'

class Song(models.Model):
    title         = models.CharField(max_length=255, null=False)
    img_link      = models.CharField(max_length=250, default="https://image.flaticon.com/icons/png/512/26/26789.png")
    link_mp3      = models.CharField(verbose_name="extra link", max_length=255, blank=True, null=True , default="") 
    date_addded   = models.DateTimeField(verbose_name="added to platform", blank=True, null=True,auto_now_add=True)
    date_updated  = models.DateTimeField(verbose_name="added to platform", blank=True, null=True, auto_now=True)

    artists       = models.ManyToManyField(Artist)
    album         = models.ForeignKey(Album, on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table = 'Songs'
    def __str__(self):
        return "{} ".format(self.title)
    
class PlayList(models.Model):
    title         = models.CharField(max_length=255, null=False)
    img_link      = models.CharField(max_length=250, default="https://visualpharm.com/assets/99/Smart%20Playlist-595b40b85ba036ed117daac8.svg")
    is_private    = models.BooleanField(default=False)
    
    
    created_by    = models.ForeignKey(User)
    date_addded   = models.DateTimeField(verbose_name="added to platform", blank=True, null=True,auto_now_add=True)
    date_updated  = models.DateTimeField(verbose_name="added to platform", blank=True, null=True, auto_now=True)
    songs         = models.ManyToManyField(Song)
    
    class Meta:
        db_table = 'PlayLists'
    def __str__(self):
        return "{} ".format(self.title)
    
    
class UserFavorites(models.Model):
    user      = models.OneToOneField(User)
    songs     = models.ManyToManyField(Song,null=True,blank=True)
    playlists = models.ManyToManyField(PlayList,null=True,blank=True)
    albums    = models.ManyToManyField(Album,null=True,blank=True)
    artists   = models.ManyToManyField(Artist,null=True,blank=True)

    class Meta:
        db_table = 'UserFavorites'
    def __str__(self):
        return "favorites of {}.{}".format(self.user.first_name,self.user.last_name)