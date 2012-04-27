#Youtube Comment Sonnet

import urllib2
from os.path import basename
from urlparse import urlsplit
from bs4 import BeautifulSoup
import re
import random

#global variables


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
 
    #Pick one of the first ten related videoes based on random number
    videoRand = random.randint(0,9)

    offset09 = data.find("related-video")
    i = 0
    while i < videoRand:
        offset09 = offset09+13 + data[offset09+13:].find("related-video")
        i = i + 1

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
	
#comment_collector: 

def comment_collector():
    site = BeautifulSoup(open("sauce.htm"))

    comArray = [None]*10
    #put all comments in comArray
    i = 0
    while i < 10: 	
        for string in site.find_all("div", "comment-text", limit = i+1):
            comArray[i] = repr(string)
        i = i + 1 

    #if comments are disabled
    if comArray[0] == None:
        nextPage = url_parser()
        website_retriever(nextPage)
        return 0

    #clean up all comments
    i = 0 
    while i < 10:
        comArray[i] = comArray[i].partition('\n<p>')[2]
        comArray[i] = comArray[i].partition('</p>\n</div>')[0]
        #account for line indents
        comArray[i] = re.sub('</p>\n<p>', " ", comArray[i])
        comArray[i] = re.sub('\xef\xbb\xbf', "", comArray[i])
        comArray[i] = re.sub('&quot;', '"', comArray[i])
        comArray[i] = re.sub('&gt;', '>', comArray[i])
        comArray[i] = re.sub('&lt;', '<', comArray[i])  
	#account for video offset links
        comArray[i] = re.sub('<a href="#" onclick="yt\.www\.watch\.player\.seekTo\(\S+\);return false;">\S+</a>', "", comArray[i])
	i = i + 1

    #send comments to be parsed and possibly written into sonnet
    i = 0
    while i < 10:
        if comment_parser(comArray[i]) != "NO_SELECT":
	    sonnet = open('sonnet.txt', 'a')	
            sonnet.seek(0, 2) #Go the the 0th byte before the end of file
            sonnet.write(comArray[i]+'\n')
	    sonnet.close()
        i = i + 1

    nextPage = url_parser()
    website_retriever(nextPage)
    return 0


def comment_parser(comment):
    if comment == None:
        return "NO_SELECT";
    else:
        return comment;

	 	




  		