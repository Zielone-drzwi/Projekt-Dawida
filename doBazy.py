from decimal import Decimal
from faker import Faker
from faker import factory
import datetime
import sqlite3

con = sqlite3.connect('fejkowa.db')
cur = con.cursor()
fake = Faker(['pl_PL'])
teraz  = datetime.datetime.now()
con.execute("""CREATE TABLE IF NOT EXISTS fejkowa
                (id  INTEGER PRIMARY KEY AUTOINCREMENT, data text, lat text, lon text, kompas INT, napiecie REAL, pochylenie INT , przechylenie INT)""")
print('Baza utworzona')
rekord = 1
for _ in range(100000):
    
    data = str(fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
    lat = str(fake.latitude())
    lon = str(fake.longitude())
    kompas = fake.random_int(min=0, max=360, step=1)
    napiecie  = (fake.random_int(min=0, max=120, step=1) / 10) #dziele zeby byly po przecinku
    przechylenie  = fake.random_int(min=0, max=90, step=1)  #te sa z dokladnoscia do stopnia
    pochylenie  = fake.random_int(min=0, max=90, step=1)  #z dokladnoscia do stopnia
    print(data, lat, lon, kompas, napiecie, przechylenie, pochylenie)
    # upload do bazy danych każdego rekordu
    parametry = (data,lat,lon,kompas,napiecie,pochylenie,przechylenie)
    con.execute("INSERT INTO fejkowa (data ,lat, lon, kompas,napiecie,pochylenie,przechylenie ) VALUES (?,?,?,?,?,?,?)",parametry)
    con.commit()
    print(rekord)
    rekord = (rekord+1)
con.close()    
# odczyt danych z bazy 
print('--------------------ODCZYT Z BAZY SQLITE---------------')
for row in con.execute("SELECT * from fejkowa"):
    print (row) 
pozniej = datetime.datetime.now()
czas = pozniej - teraz
print ('cała operacja zajęła')
print(czas)
