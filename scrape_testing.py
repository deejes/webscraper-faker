from lxml import html
import requests
from bs4 import BeautifulSoup


links = []
quotes = []
root_link = 'https://www.goodreads.com/work/quotes/3462456-the-lord-of-the-rings'



links.append(root_link)
# for x in range(2,18):
#     links.append(root_link+ "?page=" + str(x))
quotes_s = ''


for link in links:
     page = requests.get(link)
     tree = html.fromstring(page.content)
     for e in tree.xpath('//div[@class="quoteText"]/text()[1]'):
        quotes.append(e)
        # break
     break
for x in quotes:
    print (x)
    quotes_s += x + ','


soup = BeautifulSoup(quotes_s, 'html.parser')
print (soup)
