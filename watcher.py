
import sqlite3

def add_film(name, category):
    conn = sqlite3.connect('base.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO wish ('name', Комедія) VALUES ('%s', '%s')" % (name, category))
    conn.commit()
    cursor.close()
    conn.close()