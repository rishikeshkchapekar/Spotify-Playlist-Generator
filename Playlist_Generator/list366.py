import requests as req 
import random
from bs4 import BeautifulSoup as bs 

file="artist_list.txt"
covered=[]
p = open('blacklist.txt','r')
black = p.read().split("\n")
new_artists=[]
f = open(file,'r')
d=f.read()
e = d.split("\n")
count=0
for i in e:
	i = i.replace(" ","+")
	url='https://www.music-map.com/{}.html'.format(i)
	content=req.get(url)
	soup=bs(content.text,'html.parser')
	div=soup.find('div',{'id':'gnodMap'})
	try:
		hrefs=div.find_all('a')
		for hf in hrefs:
			h=hf.get_text()
			if (h not in covered) and ( h not in black):
				new_artists.append(h)
				covered.append(h)
	except Exception as err:
		print(i)
		print(err)
	

f.close()
g = open('all.txt','a')
for a in new_artists:
	g.write(a+"\n")	
g.close()
g=open('all.txt','r')
data=g.read().split("\n")			
_f = open('list366.txt','a')
done = []
while count<340:
	index = random.randint(0,len(data)-1)
	artist = data[index]
	if artist not in done:
		done.append(artist)
		_f.write(artist+"\n")
		count+=1