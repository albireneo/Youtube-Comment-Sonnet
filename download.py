#Youtube Comment Sonnet

import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup


#given a website URL, saves the source code as sauce.htm 
def website_retriever(url):	
    req = urllib2.Request(url)
    r = urllib2.urlopen(req)
    f = open("sauce.htm", 'wb')
    f.write(r.read())
    f.close()


#url_parser: finds the first related video and returns the URL 
#Does not prevent loops(i.e. video one is most related to video 2 which 
#is most related to video 1) 
def url_parser():
    youtube = "http://www.youtube.com"
    site = open("sauce.htm")
    data = site.read()
    offset09 = data.find("related-video")

    #some videos have posted video responses under "related-videos"
    #there are only two posted responses visible per page, and this 
    #filters them out  
    auxtext = data[offset09-23:offset09-9]
    if auxtext == "watch_response":
        offset09 = offset09+13 + data[offset09+13:].find("related-video")
        auxtext = data[offset09-23:offset09-9]
    if auxtext == "watch_response":
        offset09 = offset09+13 + data[offset09+13:].find("related-video")
        auxtext = data[offset09-23:offset09-9]
 
    offset2 = offset09 - 10
    offset1 = offset09 - 55 	
    end = data[offset1:offset2]
    list = end.partition('ef="')
    end = list[2] 
    final = youtube+end
    return final
	
