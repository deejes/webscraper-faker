from lxml import html
from bs4 import BeautifulSoup
import requests


links = []
quotes = []

root_link = 'https://www.goodreads.com/work/quotes/3462456-the-lord-of-the-rings'


links.append(root_link)
for x in range(2,18):
    links.append(root_link+ "?page=" + str(x))
# adds all lots page links to the links array


def quote_getter(links_array):
    for link in links:
        print (link)
        print (len(quotes))
        page = requests.get(link).content
        # gets the raw html
        soup = BeautifulSoup(page, 'html.parser')
        # parses using BeautifulSoup, overcoming encoding issues with lxml
        tree = html.fromstring(str(soup))
        # parsing stringified soup with x with lxml, allowing it to be searchable with xpath

        for e in tree.xpath('//div[@class="quoteText"]/text()[1]'):
            quotes.append(e)
        # adds individual quotes to an array. Still requires some cleaning.


quote_getter(links)


with open("lotr_quotes.txt", 'w') as out:
    for x in quotes:
        out.write(str(x) + '\n')
# writes out quotes to a txt file.
