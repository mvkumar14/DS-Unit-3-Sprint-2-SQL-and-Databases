import sqlite3
import os # used in testing stage of code

# Function to output results to txt file
def write_ans(input):
    my_file = open('answers.md','a')
    my_file.write(input)

def squery(query):
    """ Simple query format that doesn't deal with the connection object """
    output = list(curs.execute(query).fetchall())
    print(output,'\n')
    write_ans(str(output))
    write_ans('\n\n')
    return output

""" Part 1 """
write_ans('Part 1: \n')
# Create connection to demo_data
conn = sqlite3.connect('demo_data.db')

# Create cursor
curs = conn.cursor()



# Create table
curs.execute("""
    CREATE TABLE demo(
    s VARCHAR(5) PRIMARY KEY,
    x INT,
    y INT
    );
    """
    )


# Insert values into table
curs.execute("""
    INSERT INTO demo (s, x, y)
    VALUES ('g', 3, 9),
    ('v',5,7),
    ('f',8,7)
    ;""")

# Test to obtain values from table
squery('SELECT * FROM demo')

write_ans('#1: \n')
# Number of rows
squery('SELECT count(*) FROM demo')

write_ans('#2: \n')
# Rows where x and y are at least 5
squery('SELECT count(*) FROM demo WHERE x > 4 AND y > 4')

write_ans('#3: \n')
# Unique y values
squery('SELECT COUNT(DISTINCT y) FROM demo')

curs.close()
conn.commit()
conn.close()
os.remove('demo_data.db') # used in testing stage of code
