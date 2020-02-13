'''Ten skrypt ma konwertowac sql do json
'''
import datetime
import sqlite3
import json
import collections
import sys


con = sqlite3.connect('fejkowa.db')
cur = con.cursor()
teraz  = datetime.datetime.now()
con.row_factory = sqlite3.Row
#rows = cur.fetchall()
#objects_list = []  # pusta lista na odczyt z bazy
# odczyt danych z bazy 
cur.execute('''DROP TABLE IF EXISTS stocks''')
cur.execute('''CREATE TABLE stocks
                 (date text, trans text, symbol text, qty real, price real)''')

    # Insert a few rows of data.
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.0)")
cur.execute("INSERT INTO stocks VALUES ('2007-02-06','SELL','ORCL',200,25.1)")
cur.execute("INSERT INTO stocks VALUES ('2008-03-06','HOLD','IBM',200,45.2)")
con.commit()
print('--------------------ODCZYT Z BAZY SQLITE---------------')
'''
for rows in con.execute("SELECT * from fejkowa LIMIT 0,30"): # limit zeby szybciej zobaczyc efekt
    d = collections.OrderedDict()
    d['ID'] = (rows[0]) 
    d['data'] = (rows[1]) 
    d['lat'] = (rows[2]) 
    d['lon'] = (rows[3]) 
    d['kompas'] = (rows[4]) 
    d['napiecie'] = (rows[5]) 
    objects_list.append(d)
    print (rows[1]) 
    print (rows[2]) 
    print (rows[3]) 
    print (rows[4]) 
    print (rows[5]) 
    print(objects_list)

# przerobienie

#j = json.dumps(objects_list)
#rowarrays_file = 'json.json'
#f = open(rowarrays_file,'w')
# Konwesja do gotowego do json
pozniej = datetime.datetime.now()
czas = pozniej - teraz
print ('cała operacja zajęła', czas)  

'''

cur.execute("SELECT * FROM stocks")
recs = cur.fetchall()
print (recs)
print ("DB data as a list with a dict per DB record:")
rows = [ dict(rec) for rec in recs ]
print (rows)
print
print ("DB data as a single JSON string:")
rows_json = json.dumps(rows)
print (rows_json)