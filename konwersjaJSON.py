'''Ten skrypt ma konwertowac sql do json
'''
import datetime
import sqlite3

con = sqlite3.connect('fejkowa.db')
cur = con.cursor()
teraz  = datetime.datetime.now()

# odczyt danych z bazy 
print('--------------------ODCZYT Z BAZY SQLITE---------------')
for row in con.execute("SELECT * from fejkowa LIMIT 0,300"): # limit zeby szybciej zobaczyc efekt
    print (row) 


pozniej = datetime.datetime.now()
czas = pozniej - teraz
print ('cała operacja zajęła')
print(czas)
