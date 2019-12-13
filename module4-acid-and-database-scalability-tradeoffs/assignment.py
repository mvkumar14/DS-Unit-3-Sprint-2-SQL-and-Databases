""" Module 4 Assignment """

import psycopg2
import sqlite3
import pandas as pd
from mod4_functions import *

# I created the connection to my server and created functions to
# retreive sql query results in mod4_functions.

""" PART 1 using psychopg2 and elephantsql to traverse titanic.csv """

# If you are unsure of what is in the database check tables with this:
pg_query('SELECT tablename FROM pg_tables')

# This is how you get the column names from a table
pg_queryv("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'titanic';")
