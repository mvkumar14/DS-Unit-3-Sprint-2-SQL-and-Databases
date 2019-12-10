import sqlite3
import pandas as pd

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")

a = pd.read_sql('{name}',conn)
print(a)







#
#
# query = ('SELECT *' +
#     'FROM charactercreator_character_inventory GROUP BY character_id')
#
#
# curs = conn.cursor()
# print(curs.execute(query).fetchall())
