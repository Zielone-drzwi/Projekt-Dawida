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