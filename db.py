# -*- coding:utf-8 -*-
import sys, sqlite3, time, os
reload(sys)
sys.setdefaultencoding("utf-8")

path = os.getcwd()+"/"

date = time.strftime("%d%m%y")
#sql connection
con = sqlite3.connect(path+"databases/"+"feed",check_same_thread=False)
first = [	"CREATE TABLE spectrum%s(sira INTEGER PRIMARY KEY AUTOINCREMENT, giri,link,zaman)"%date,
			"CREATE TABLE ycombinator%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE newyorker%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE verge%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE arstechnica%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE bbc%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE nature%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE cell%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE guardian%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE aljazeera%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE reuters%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE timemag%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE streamfiyat%s(sira INTEGER PRIMARY KEY AUTOINCREMENT,giri,link,zaman)"%date,
			"CREATE TABLE test%s(deger,zaman)"%date]

tables = []
for elems in first:
	tables.append(elems.split(" ")[2].split("(")[0])

# time thing
def now():
	return time.strftime("%H:%M:%S %d/%m/%y")

try:
	with con:
		cursor = con.cursor()
		simdi = now()
		cursor.execute("INSERT INTO test(deger,zaman) VALUES(1,'%s')"%simdi)
except:
	with con:
		cursor = con.cursor()
		for cmd in first:
			cursor.execute(cmd)

def escapist(data):
	asd = []
	for cur in data:
		try:
			if cur not in "\'\"`\n\t":
				asd.append(cur)
		except:
				if cur in "\'\"`":
					asd.append("^")
	return "".join(asd)



def push_unsecure(table_name,giri,link):
	zaman = now()
	with con:
		cur = con.cursor()
		giri = escapist(giri)
		link = escapist(link)
		cur.execute("INSERT INTO %s(giri,link,zaman) VALUES(\'%s\',\'%s\',\'%s\')"%(table_name,giri,link,zaman))

def pushc(table_name,giri,link):
	with con:
		cursor = con.cursor()
		giri = escapist(giri)
		link = escapist(link)
		tete = cursor.execute("""SELECT * FROM %s WHERE giri=\'%s\'"""%(str(table_name),str(giri))).fetchall()
		if tete == []:
			push_unsecure(table_name,giri,link)

def querries():
	dicts = {}
	with con:
		cur = con.cursor()
		for table_name in tables:
			data = cur.execute("SELECT * FROM %s"%table_name).fetchall()
			dicts.update({table_name:data})
	return dicts

def test():
	with con:
		cur = con.cursor()
		for table in tables:
			print table, len(cur.execute("SELECT * FROM %s"%table).fetchall())

