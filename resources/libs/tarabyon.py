from bs4 import BeautifulSoup
import requests, re,json

from resources.models import *

class Source:
    url="https://www.tarabyon.com/en/"
    url_artist = "https://www.tarabyon.com/en/artists.asp?artistid={}"
    def __init__(self, source_id=None):
        pass
    
    def getDataFromArtist(self,artist_id):
        output = {"success": False, "data": [], "error": None}
        response = requests.get(self.url_artist.format(artist_id))
        self.soup = BeautifulSoup(response.content , "html5lib")
        output["data"] = self.get_artist()
        return output
        
    def get_artist(self):
        """
        img     = self.soup.find_all('aside', class_='aside-lg')[0].find_all("a", class_="thumb-lg")[0].find_all('img')[0]["src"]
        name    = self.soup.find_all('aside', class_='aside-lg')[0].find_all("div", class_="artist-header")[0].text
        country = self.soup.find_all('aside', class_='aside-lg')[0].find_all(class_="text-center")[0].find_all(class_="text-muted")[0].text
        """
        # ---------- Artist
        artist = {}
        print(self.toBS(".aside-lg .thumb-lg img"))
        artist["img_link"] = self.toBS(".aside-lg .thumb-lg img")[0]["src"]
        artist["full_name"]  = self.toBS(".aside-lg .artist-header")[0].text
        artist["country"]  = self.toBS(".aside-lg .text-center .text-muted")[0].text
        
        artist = Artist.create(**artist)
        artist.save()
        albums = []
        
        albums_elements = self.toBS("#albums .padder-lg-2 .row .col-md-12 .row .col-xs-6")
        
        for album_obj in albums_elements:
            # ---------- Albums
            album_dict = {}
            album_dict["date_release"]  = self.toBS("a.text-ellipsis span", album_obj)[0].text
            album_dict["title"] = self.toBS("a.text-ellipsis", album_obj)[0].text[:-4]
            link = self.toBS("a.text-ellipsis", album_obj)[0]["href"]
            album_dict["img_link"]   = self.toBS("a img", album_obj)[0]["src"]

            # ---------- Song
            print(self.url+link)
            response = requests.get(self.url+album_dict["link"])
            soup_song = BeautifulSoup(response.content , "html5lib")
            #songs_elements = self.toBS("#One .list-group-item a.jp-play-me", soup_obj=soup_song)
            songs_elements = self.toBS(".active .list-group-item a.jp-play-me", soup_obj=soup_song)
            songs = []
            print( len(list(songs_elements)))
            for song_ele in songs_elements:
                songs.append( {"title":song_ele["title"], "link_mp3":song_ele["data-jp-src"]} )


            album_dict["songs"] = songs
            albums.append(album_dict)
        
        artist["albums"] = albums
        return json.dumps(artist)
        
    def toBS(self,selector,soup_obj=None):
        output = ""
        selector_conds = selector.split(" ")
        soup_set = [self.soup,] if soup_obj==None else [soup_obj,]
        for sl in selector_conds:
            
            sl_cls = sl.split(".")
            sl_id = sl.split("#")
            
            soup_set_new=[]
            for soup_ele in soup_set:
                if soup_ele == None : continue
                soup_ch = False
                if len(sl_cls) == 1 and len(sl_cls) == 1:
                     soup_ch=soup_ele.find_all(sl)
                if len(sl_cls) == 2:
                    if sl[0]==".":
                        soup_ch=soup_ele.find_all(class_=sl_cls[1])
                    else:
                        soup_ch=soup_ele.find_all(sl_cls[0], class_=sl_cls[1])
                elif len(sl_id) == 2:
                    if sl[0]=="#":
                        soup_ch=[soup_ele.find(id=sl_id[1]),]
                    else:
                        soup_ch=[soup_ele.find(sl_cls[0], id=sl_id[1]),]
                if len(sl_cls) == 3:
                    if sl[0]==".":
                        soup_ch=soup_ele.find_all(class_=[sl_cls[1],sl_cls[2]])
                    else:
                        soup_ch=soup_ele.find_all(sl_cls[0], class_=[sl_cls[1],sl_cls[2]])

                if soup_ch :
                    soup_set_new += list(soup_ch)
                
            soup_set = soup_set_new
        return soup_set