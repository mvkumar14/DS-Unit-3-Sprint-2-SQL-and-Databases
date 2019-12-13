import sqlite3

# For formatting in terminal
print('\n\n')

# Function to output results to txt file
def write_ans(input):
    my_file = open('answers.md','a')
    my_file.write(input)

# Simple query function
def squery(query):
    """ Simple query format that doesn't deal with the connection object """
    output = list(curs.execute(query).fetchall())
    print(output,'\n')
    write_ans(str(output))
    write_ans('\n\n')
    return output

"""--------------------------- Part 2 ----------------------------"""
write_ans('Part 2: \n')
# Create connection to demo_data
conn = sqlite3.connect('northwind_small.sqlite3')

# Create cursor
curs = conn.cursor()

# Showing table columns:
print(list(curs.execute("""SELECT name FROM sqlite_master WHERE type='table' ORDER BY
name;""").fetchall()))

write_ans('#1: \n')
# Ten most expensive items (per unit price) in database
squery('SELECT productname,unitprice FROM product ORDER BY unitprice DESC LIMIT 10')

write_ans('#2: \n')
# Average age of employee at time of hiring
squery('SELECT AVG(hiredate-birthdate) AS startage FROM employee')


"""--------------------------- Part 3 ----------------------------"""
write_ans('Part 3: \n')
# Ten most expensive items in database and their suppliers' names
write_ans('#1: \n')
squery("""
    SELECT supplier.companyname,product.productname,product.unitprice
    FROM product
    INNER JOIN supplier ON supplierid=supplierid
    ORDER BY unitprice DESC LIMIT 10
    ;""")

# Largest category
write_ans('#2: \n')
squery("""
    SELECT categoryname,count(DISTINCT productname)
    FROM product
    LEFT JOIN category
    ON category.id = product.categoryid
    GROUP BY categoryname
    ORDER BY count(*) DESC
    LIMIT 1
    ;""")

curs.close()
conn.close()
