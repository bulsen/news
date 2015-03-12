# -*- coding: utf-8 -*-
import sys , requests, bs4, db, time,re
reload(sys)
sys.setdefaultencoding("utf-8")

def is_link(site,link):
	if link[:4] =="http":
		return link
	elif link[:4] == "www.":
		return link
	elif link:
		return site+link


def streamfiyat():
	data = requests.get("http://www.vatanbilgisayar.com/hp-stream-13-c000nt-celeron-n2840-216ghz-2gb-32gb-ssd-133-int-w81-notebook.html?srt=UP#genel-bakis").text

	bs = bs4.BeautifulSoup(data)

	arr=[]
	for elems in bs.find_all("span"):
		if re.match("[0-9][0-9][0-9]\,[0-9]*",elems.match)
			arr.append(elems.text)

	db.pushc("streamfiyat",arr[1],"lol")

def crawl():

	sites =[	{"db":"spectrum","link":"http://spectrum.ieee.org/","buff":23},
				{"db":"ycombinator", "link":"http://news.ycombinator.com","buff":12},
				{"db":"newyorker", "link":"http://www.newyorker.com/","buff":23},
				{"db":"verge", "link":"http://www.theverge.com/","buff":30},
				{"db":"guardian", "link":"http://www.theguardian.com/uk","buff":23},
				{"db":"arstechnica", "link":"http://www.arstechnica.com","buff":23},
				{"db":"bbc", "link":"http://www.bbc.co.uk","buff":23},
				{"db":"nature", "link":"http://www.nature.com","buff":23},
				{"db":"cell", "link":"http://www.cell.com","buff":23},
				{"db":"aljazeera", "link":"http://www.aljazeera.com/","buff":23},
				{"db":"timemag", "link":"http://www.time.com","buff":23},
				{"db":"reuters", "link":"http://www.reuters.com","buff":23}]

	doop =[]
	for lines in open("pepe"):
		doop.append(lines[:-1])

	for dicts in sites:
		print dicts["db"], time.strftime("%H:%M:%S")
		data = requests.get(dicts["link"]).text
		bs = bs4.BeautifulSoup(data)

		for a in bs.find_all("a",href=True):
			if a.text not in doop:
				#print capsule
				link = is_link(dicts["link"],a["href"])
				if len(a.text) > dicts["buff"]:
					db.pushc(dicts["db"],str(a.text).encode("utf-8"),link)

while 1:
	crawe = ["00:00","8:42","9:15","11:35","14:00","15:13","18:17","20:13"]
	if str(time.strftime("%H:%M")) in crawe:
		crawl()
		
	elif str(time.strftime("%M")) =="00":
		streamfiyat()
