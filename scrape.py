#webscraping: imdb top 250 movie list

from bs4 import BeautifulSoup
import urllib2
url="http://www.imdb.com/chart/top"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read(),"lxml")
data = []
info = []
table = soup.find('table', attrs={'class':'chart'})
table_body = table.find('tbody')

rows = table_body.findAll('tr')
i=0
for row in rows:
    cols = row.find('td',attrs={'class':'titleColumn'})
    if i<10:
    	print cols.a.string
	link = "http://www.imdb.com" + cols.a["href"]
	inside = urllib2.urlopen(link)
	new_soup=BeautifulSoup(inside.read(),"lxml")
	spans=new_soup.find('span',attrs={'class':'see-more inline'})
	'''
	for span in spans:
   		 links = span.findAll('a')
   		 for link in links:
	for links in spans:
		for link in links.findAll('a'):
        		print(link['href'])   
	'''
	#category_links = [a["href"] for a in new_class.findAll("a")]	
	anchors=spans.findAll('a')
	print anchors[0]
	print anchors[1]
	synopsis=anchors[1]["href"]
	print synopsis
	i=i+1
    else:
	break
