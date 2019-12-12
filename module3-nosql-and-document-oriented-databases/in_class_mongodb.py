import pymongo

username = 'your_username'
password = 'your_password'

client = pymongo.MongoClient("mongodb://admin:<password>@cluster0-shard-00-00-8imhl.mongodb.net:27017,cluster0-shard-00-01-8imhl.mongodb.net:27017,cluster0-shard-00-02-8imhl.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

print(db)
# Doesn't print anything here
print(client.nodes)

db.test.insert_one({'x':1})
db.test.update_one({'x':1},{'$inc':{'x':5}})
print(list(db.test.find()))

# Define a new batch of documents for an insert_many command
stephanie_doc = {
    'favorite animal':'alpaca',
    'favorite color':'blue'
}

zoli_michelle_doc = {
    'favorite animal': ['Black Panther','Unicorn']
}

dorothy_doc = {
    'favorite animal':'dog'
}

# Insert the created documents into the database
db.test.insert_many([stephanie_doc,zoli_michelle_doc,dorothy_doc])

# Look at all the documents
print(list(db.test.find()))

# Make more documents with a for loop
# This is a list of documents
more_docs = []
for i in range(10):
    # First we will make a document within the loop
    doc = {'even':i%2 == 0}
    doc['value'] = i
    # Then add the information of the "document" to the list.
    more_docs.append(doc)

# Now more_docs has information in it, that can be put into the # DEBUG:
# print(more_docs)

# Input to database
db.test.insert_many(more_docs)

# Show the evens from the generated docs:
print(list(db.test.find({'even':False})))

# Update many with an increment
db.test.update_many({'even':True},{'$inc':{'value':100}})

# Add rpg_character
rpg_character = (1,'King Bob',10,3,0,0,0)

# You would get an error if you just tried to plug this in.
# You need to cast to a dictionary and then upload the dictionary.
db.test.insert_one({'rpg_character':rpg_character})

# A New dictionary that defines the structure of rpg_character
db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

# Show state at the end of the file
print('\n\n')
# A function to display the current database in a pretty format inside of
# terminal would be very useful here.
print((list(db.test.find())))

# Delete everything at the end of the script so when it is run again, it runs
# properly
db.test.delete_many({})

# After a command, however, it prints properly.
# print(client.nodes)
