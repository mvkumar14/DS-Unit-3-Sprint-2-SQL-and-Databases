""" Module 4 Assignment """

import psycopg2
import sqlite3
import pandas as pd
from mod4_functions import *

# I created the connection to my server and created functions to
# retreive sql query results in mod4_functions.

""" PART 1 using psychopg2 and elephantsql to traverse titanic.csv """

# If you are unsure of what is in the database check tables with this:
pg_query('SELECT tablename FROM pg_tables;')

# This is how you get the column names from a table
pg_queryv("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'titanic';")

pg_queryv("SELECT * FROM titanic LIMIT 1;")

# 1 number alive/dead
print("1")
alive = pg_query("SELECT count(*) FROM titanic WHERE survived = 0")
dead = pg_query('SELECT count(*) FROM titanic WHERE survived = 1')
print('alive: ',alive[0][0], 'dead: ',dead[0][0])

# 2 passengers in each class
print("2")
pg_queryv('SELECT pclass,count(*) FROM titanic GROUP BY pclass ORDER BY pclass')

# 3 How many passengers survived/died within each class?
print("3")
pg_queryv("""SELECT pclass,survived,count(survived)
    FROM titanic
    GROUP BY pclass,survived
    ORDER BY pclass,survived;""")

# 4 Average age of survivors vs nonsurvivors
print("4")
pg_queryv('SELECT AVG(age) FROM titanic WHERE survived = 0')
pg_queryv('SELECT AVG(age) FROM titanic WHERE survived = 1')

# 5 Average age of each passenger class
print("5")
pg_queryv('SELECT pclass,AVG(age) FROM titanic GROUP BY pclass ORDER BY pclass')

# 6 Average fare by passenger class
print("6")
print('by class:')
pg_queryv('SELECT pclass,avg(fare) FROM titanic GROUP BY pclass ORDER BY pclass')
print('by survival:')
pg_queryv('SELECT survived,avg(fare) FROM titanic GROUP BY survived ORDER BY survived')

# 7 Average fare by survival
print("7")
pg_queryv('SELECT AVG(siblings_spouses_aboard) FROM titanic;')
pg_queryv("""SELECT pclass,AVG(siblings_spouses_aboard) FROM titanic
    GROUP BY pclass
    ORDER BY pclass;""")
pg_queryv("""SELECT survived,AVG(siblings_spouses_aboard) FROM titanic
    GROUP BY survived
    ORDER BY survived;""")
# 8
print('8')
pg_queryv('SELECT AVG(parents_children_aboard) FROM titanic;')
pg_queryv("""SELECT pclass,AVG(parents_children_aboard) FROM titanic
    GROUP BY pclass
    ORDER BY pclass;""")
pg_queryv("""SELECT survived,AVG(parents_children_aboard) FROM titanic
    GROUP BY survived
    ORDER BY survived;""")

# 9
print('9')
a = pg_query('SELECT count(name) FROM titanic')
a = a[0][0]
print(a)
b = pg_query('SELECT count(DISTINCT name) FROM titanic')
print(b)
