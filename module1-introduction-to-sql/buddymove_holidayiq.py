import pandas as pd
import sqlite3

def mktableq(name):
    query = "CREATE TABLE " + name + ";"
    return query

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')
curs = conn.cursor()

df.to_sql('3',conn)

print(curs.execute("SELECT *;").fetchall())
