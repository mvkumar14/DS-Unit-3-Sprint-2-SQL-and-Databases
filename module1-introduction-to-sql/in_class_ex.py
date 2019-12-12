
import sqlite3
import os
import time

#Creating a connection object
conn = sqlite3.connect('toy_data.db')

#Be able to see the directory from within the python file
print(os.listdir())

# writing out a command for the sql db that we created
query = 'CREATE TABLE toy (name varchar(30),size int);'

# creating an object to interact with db
curs = conn.cursor()
print(dir(curs))

# executing the query
curs.execute(query)

# closing the cursor, and commiting the changes.
curs.close()
conn.commit()

# opening new cursor, and trying to access informtion from the db
curs2 = conn.cursor()
curs2.execute('SELECT * FROM toy;').fetchall()

# adding a value to the table
insert_query = "INSERT INTO toy (name,size) VALUES ('AWESOME',27);"

# closing and saving the cursor
curs2.execute(insert_query)
curs2.close()
conn.commit()

# opening third cursor, and checking that the changes saved
curs3 = conn.cursor()
print(curs3.execute('SELECT * FROM  toy;').fetchall())
curs3.close()
conn.commit()

conn.close()
# time.sleep(1)
os.remove('toy_data.db')
