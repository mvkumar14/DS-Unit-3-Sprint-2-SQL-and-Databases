import psycopg2

# Credentials:
dbname = 'ifoxvihb'
user = 'ifoxvihb'
password = 'q6Wb5q4ngbTtETbu5oq8QqgT4Q5PSaIi'
host = 'rajje.db.elephantsql.com'

# Create connection:
pg_conn = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host
)

# function to abstract away the details of a query.
# this one prints out the result
def pg_queryv(query):
    """ Function to abstract away details of querying database
    Inputs:
    query - your SQL query

    Output:
    Terminal should print the result, and the result of the query will be
    returned
    """
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    result = pg_curs.fetchall()
    pg_curs.close()
    print(result)
    return result

# This one doesn't print the output.
def pg_query(query):
    """ Function to abstract away details of querying database
    Inputs:
    query - your SQL query

    Output:
    Result of the query
    """
    pg_curs = pg_conn.cursor()
    pg_curs.execute(query)
    result = pg_curs.fetchall()
    pg_curs.close()
    return result

# If this was in a class I would still have two functions that would inherit
# from a base class (_query_base) that would
# additionally I would have a "close"

# Really the trend I'm noticing here is that during development I want feedback,
# but after the feedback, and after I understand the mechanisms to some
# extent I no longer need the verbosity. A debugger solves this problem to some
# degree because it gives me access directy to the variable/ state values,
# but its not quick. If I want to iterate quickly something like an ipython
# notebook is best, and then when I want to finalize the implimentation I'll
# turn it into less "code to check implimentation" and just implimentation
# The problem is that an ipython notebook doesn't always have the same environment
# as this atom editor? (Maybe I can just open an ipython notebook in atom?)
