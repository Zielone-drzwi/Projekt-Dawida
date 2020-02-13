'''Ten skrypt ma konwertowac sql do json
'''
import datetime
import sqlite3
import json
import collections

con = sqlite3.connect('fejkowa.db')
cur = con.cursor()
teraz  = datetime.datetime.now()
#rows = cur.fetchall()
objects_list = []  # pusta lista na odczyt z bazy
# odczyt danych z bazy 
print('--------------------ODCZYT Z BAZY SQLITE---------------')
for rows in con.execute("SELECT * from fejkowa LIMIT 0,300"): # limit zeby szybciej zobaczyc efekt
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


# Convert query to row arrays
rowarray_list = []
for row in rows:
    t = (row.ID, row.data, row.lat, 
         row.lon, row.kompas, row.napiecie, row.pochylenie, row.przechylenie)
    rowarray_list.append(t)
    
j = json.dumps(rowarray_list)
rowarrays_file = 'student_rowarrays.txt'
f = open(rowarrays_file,'w')
# Konwesja do gotowego do json
objects_list = []
for row in rows:
    d = collections.OrderedDict()
    d['id'] = row.ID
    print(d['id'])
    d['data'] = row.data
    d['lat'] = row.lat
    d['lon'] = row.lon
    d['kompas'] = row.kompas
    d['napiecie'] = row.napiecie
    d['pochylenie'] = row.pochylenie
    d['przechylenie'] = row.przechylenie
    objects_list.append(d)
j = json.dumps(objects_list)
objects_file = 'student_objects.txt'
f = open(objects_file,'w')
#print (f,j)



pozniej = datetime.datetime.now()
czas = pozniej - teraz
print ('cała operacja zajęła')
print(czas)
