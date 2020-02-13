

import sys
import sqlite3
import json
import os   

try:

    conn = sqlite3.connect('fejkowa.db')

    # włacza odczyt w kolumnach
    conn.row_factory = sqlite3.Row

    curs = conn.cursor()

   

    # odczyt bazy danych 
    curs.execute("SELECT * FROM fejkowa LIMIT 0,30")
    recs = curs.fetchall()

    
    rows = [ dict(rec) for rec in recs ]
    #print (rows)

    print

    print ("tu ma pojawić sie json , terst")
    rows_json = json.dumps(rows)
    print (rows_json)
    with open('jsonik.json', 'w') as f:
        f.write(rows_json)

except Exception:
    print ("Wystąpił błąd..") 
    
    sys.exit(1)