# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import urllib2

BASE_URL = 'https://www.vangoghmuseum.nl'
LIST_URL = BASE_URL+'/en/search/collection?q=&artist=Vincent%20van%20Gogh&pagesize=996'


def file_download(url):    
    file_name = 'picture/'+(url.split('/')[-1].split('?')[0])
    u = urllib2.urlopen(url)
    with open(file_name, 'wb') as f:
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,



def get_html(url):
   _html = ""
   resp = requests.get(url)
   if resp.status_code == 200:
      _html = resp.text
   return _html


def main():
   html = get_html(LIST_URL)
   soup = BeautifulSoup(html, 'html.parser')
   ids = soup.findAll("a", {"class":["link-teaser", "triggers-slideshow-effect"]}) 
   for id in ids:
        time.sleep(1)
        detail_url = BeautifulSoup(get_html(BASE_URL + id["href"]), 'html.parser').find("a", {"class":["button.dark-hover", "rounded-right"]})
        if detail_url is not None:
            file_download(BASE_URL+detail_url["href"])
        


if __name__ == "__main__":
    main()
