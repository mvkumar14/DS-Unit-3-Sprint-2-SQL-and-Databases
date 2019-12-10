import psycopg2
import sqlite3
import pandas as pd

# This information is from the details panel of the elephantsql console
dbname= "your_db_name"
user = "your_user"
password = "your_password"
host = "your_host"


""" Step 1: Creating an elephantsql connection """
# Creating an ElephantSQL connection
pg_conn = psycopg2.connect(
    dbname = dbname,
    user = user,
    password = password,
    host = host
)

#Create cursor for pg (elephantsql)
pg_curs = pg_conn.cursor()


""" Step 2: loading the data into a sqlite database """
# Creating a sqlite 3 database for titanic.csv
sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

# Read data into a dataframe
t = pd.read_csv('titanic.csv')

# How many characters needed for the varchar in name
# The script returns 82 but I round up to 90 below.
print(max(t.Name.apply(lambda x: len(x))))

# Turn data into a sql table
t.to_sql("titanic",sl_conn,if_exists='replace')

# Retrive and print the first 5 columns of the databse
# print(sl_conn.execute('SELECT * from titanic LIMIT(5);').fetchall())

# Getting information about the datatypes using PRAGMA (only sqlite3)
# print(sl_conn.execute('PRAGMA table_info(titanic);').fetchall())


""" Step 3: setting up table for elephantsql """

mk_table_titanic = """
    CREATE TABLE titanic(
    index SERIAL PRIMARY KEY,
    Survived INT,
    Pclass INT,
    Name VARCHAR(90),
    Sex VARCHAR(10),
    Age INT,
    Siblings_Spouses_Aboard INT,
    Parents_Children_Aboard INT,
    Fare INT
    );
    """
# I want to try using the following for Sex:
# CREATE TYPE sex AS ENUM ('male','female'),

""" Step 4: creating table/adding values in the elephantsql db using pg_curs """
# Making the table with pg_curs
pg_curs.execute(mk_table_titanic)

# Function to display the tables in the database Only works for pgsql
# May not be super necessary right here right now, but useful when in terminal
# with this file.
def show_tables(cursor):
    tables = """
        SELECT *
        FROM pg_catalog.pg_tables
        WHERE schemaname != 'pg_catalog'
        AND schemaname != 'information_schema';
        """
    cursor.execute(tables)
    print(cursor.fetchall())

# Uncomment to see the tables in a pgsql db
# show_tables(pg_curs)

# TRYING TO INSERT ALL INSTEAD OF LOOPING

# Testing that string composition for INSERT INTO works:
titanic_rows = sl_curs.execute('SELECT * FROM titanic').fetchall()
print(','.join(f'{x}' for x in titanic_rows[0:5]))

# For INSERT INTO
# This solution comes from : https://stackoverflow.com/a/10147451
titanic_data_sql = ','.join(f'{x}' for x in titanic_rows)

# query to insert data into postgresql database
titanic_insert = """
    INSERT INTO titanic
    (index, Survived, Pclass, Name, Sex, Age,
    Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
    VALUES
    """ + titanic_data_sql + ';'

pg_curs.execute(titanic_insert)

pg_curs.execute('SELECT count(*) FROM titanic')
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()


# DEBUG CODE FOR the ' issue.

# # If you want to prove that the function doesn't work for sql
# show_tables(sl_curs)

# titanic_rows = sl_curs.execute('SELECT * FROM titanic').fetchall()
# titanic_insert = """
#     INSERT INTO titanic
#     (index, Survived, Pclass, Name, Sex, Age,
#     Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
#     VALUES
#     """ + str(titanic_rows[29]) + ';'
# pg_curs.execute(titanic_insert)
# pg_curs.execute('SELECT * from titanic')
# print(pg_curs.fetchall())
#
# for row in titanic_rows:
#     titanic_insert = """
#         INSERT INTO titanic
#         (index, Survived, Pclass, Name, Sex, Age,
#         Siblings_Spouses_Aboard, Parents_Children_Aboard, Fare)
#         VALUES
#         """ + str(row) + ';'
#     pg_curs.execute(titanic_insert)
