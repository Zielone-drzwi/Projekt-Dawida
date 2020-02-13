from decimal import Decimal
from faker import Faker
from faker import factory
import datetime
import sqlite3

con = sqlite3.connect('fejkowa.db')
cur = con.cursor()
fake = Faker(['pl_PL'])

con.execute("""CREATE TABLE IF NOT EXISTS fejkowa
                (id  INTEGER PRIMARY KEY AUTOINCREMENT, data text, lat text, lon text, kompas INT, napiecie REAL, pochylenie INT , przechylenie INT)""")
print('Baza utworzona')
for _ in range(10):
    data = str(fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None))
    lat = str(fake.latitude())
    lon = str(fake.longitude())
    kompas = fake.random_int(min=0, max=360, step=1)
    napiecie  = (fake.random_int(min=0, max=120, step=1) / 10) #dziele zeby byly po przecinku
    przechylenie  = fake.random_int(min=0, max=90, step=1)  #dziele zeby byly po przecinku
    pochylenie  = fake.random_int(min=0, max=90, step=1)  #dziele zeby byly po przecinku
    print(data, lat, lon, kompas, napiecie, przechylenie, pochylenie)
    # upload do bazy danych każdego rekordu
    parametry = (data,lat,lon,kompas,napiecie,pochylenie,przechylenie)
    con.execute("INSERT INTO fejkowa (data ,lat, lon, kompas,napiecie,pochylenie,przechylenie ) VALUES (?,?,?,?,?,?,?)",parametry)
    con.commit()