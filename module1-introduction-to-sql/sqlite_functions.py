import sqlite3

def query(x,db,v=True):
    """ A function that takes in a query and returns/ prints the result"""
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    my_result = list(curs.execute(x).fetchall())
    curs.close()
    conn.commit()
    if v is True:
        print(my_result)
    return my_result

query("SELECT * FROM charactercreator_character",'rpg_db.sqlite3')
