from lxml import html
from bs4 import BeautifulSoup
import requests


links = []
quotes = []

root_link = 'https://www.goodreads.com/work/quotes/3462456-the-lord-of-the-rings'

page = requests.get(root_link).content
# gets the raw html
soup = BeautifulSoup(page, 'html.parser')
# parses using BeautifulSoup, overcoming encoding issues with lxml
tree = html.fromstring(str(soup))
# parsing stringified soup with x with lxml, allowing it to be searchable with xpath

for e in tree.xpath('//div[@class="quoteText"]/text()[1]'):
    quotes.append(e)
# adds individual quotes to an array. Still requires some cleaning.

for q in quotes:
    print (q)
