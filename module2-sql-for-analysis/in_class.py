import psycopg2
import sqlite3
import imp

# This information is from the details panel of the elephantsql console
dbname = "your_db_name"
user = "your_user"
password = "your_password"
host = "your_host"


# Creating an ElephantSQL connection
pg_conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host)

# Create cursor
pg_curs = pg_conn.cursor()

# Execute query and return result. (ESQL requires second line)
pg_curs.execute('SELECT * FROM test_table;')
print(pg_curs.fetchall())


# Get information about rpg_db
sl_conn = sqlite3.connect('rpg_db.sqlite3')
sl_curs = sl_conn.cursor()

# Example query
print(sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall())

# This is what I want to transfer to ESQL
characters = sl_curs.execute("SELECT * from charactercreator_character").fetchall()
print(characters[0])

a = sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()
print(a)


create_character_table = """
    CREATE TABLE charactercreator_character(
        character_id SERIAL PRIMARY KEY,
        name varchar(40),
        level int,
        exp int,
        hp int,
        strength int,
        intelligence int,
        dexterity int,
        wisdom int
        );
    """
# Rerun the following 3 lines if table was deleted
# pg_curs.execute(create_character_table)
# pg_conn.commit()

show_tables = """
    SELECT *
    FROM pg_catalog.pg_tables
    WHERE schemaname != 'pg_catalog'
    AND schemaname != 'information_schema';
    """


pg_curs.execute(show_tables)
print(pg_curs.fetchall())


# When you need to delete the table for whatever reason
# pg_curs.execute('DROP TABLE charactercreator_character;')

example_insert = """
    INSERT INTO charactercreator_character
    (name, level, exp, hp, strength, intelligence, dexteirty, wisdom) VALUES
    """ + str(characters[0][1:]) + ";"

for character in characters:
    insert_character = """
        INSERT INTO charactercreator_character
        (name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES
        """ + str(character[1:]) + ";"
    pg_curs.execute(insert_character)

pg_curs.execute("SELECT * FROM charactercreator_character")
print(pg_curs.fetchall())

pg_curs.close()
pg_conn.commit()
