from bs4 import BeautifulSoup
from htmlparser import get_price
import urllib2
import re


seed_url = "https://www.goodreads.com/work/quotes/3462456-the-lord-of-the-rings"

# def get_html(url):
#     htmlfile = urllib2.urlopen(url)
#     htmltext = htmlfile.read(htmlfile)
#     print (get_name(htmltext) + " : " +get_price(htmltext))

def get_links(url):
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    #return an array of all the links from a given url
    all_links = []
    html_page = urllib2.urlopen(url,"lmxl")
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a'):
        all_links.append(link.get('href'))
    # print len(all_links)
    # test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
    # alias ls='ls --color=auto'
    #alias dir='dir --color=auto'
    #alias vdir='vdir --color=auto'
    # print "You scraped", len(all_links), "links."
    return all_links


print (get_links(seed_url))
