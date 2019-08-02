
import sys, os, copy, datetime, django


sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))    
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mscfy.settings")
django.setup()

from optparse import OptionParser
from resources.models import *
import resources.libs.tarabyon as tarabyon

#print(Album.objects.all())


class MediaScrapper:
    sources=[tarabyon,]
    def __init__(self, source_id=None):

        self.obj = self.sources[source_id].Source()
        
        print(self.obj.getDataFromArtist(653))
    
    
MediaScrapper(0)