from bot import*
import sqlite3

def add_film(name):
    conn = sqlite3.connect('base.sqlite')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO wish (name, Комедія) VALUES ('%s', '%s')" % (name))
    conn.commit()
    cursor.close()
    conn.close()