import os
import sqlite3



# this only works when the cursor is curs, but the cursor can be turned into
# an input variable to make the function more general.
def amt(query):
    return len(curs.execute(query).fetchall())

conn = sqlite3.connect("rpg_db.sqlite3")
query = 'SELECT * FROM charactercreator_character;'


curs = conn.cursor()
# 1 Total characters:
print("Total characters:", len(curs.execute(query).fetchall()),'\n')

# 2 Number of each subclass:
char_list = ['mage','necromancer','thief','cleric','fighter']

for i in char_list:
    my_query = 'SELECT * FROM charactercreator_' + i + ';'
    print(i.upper(),":", amt(my_query))

# 3 Number of items
item_query = "SELECT * FROM armory_item"
print("\nTotal items:", amt(item_query))

# 4 Number of Weapon items
weapon_items = 'SELECT * FROM armory_weapon'
print('\nTotal weapons:', amt(weapon_items))

# 5 Number of non-weapon items
print("\nTotal non-weapons", amt(item_query)-amt(weapon_items))

# 6 How many items does each character have.
# The following is the naive way to get the information needed:
for i in range(1,20):
    num_items = f'SELECT * FROM charactercreator_character_inventory WHERE' +
        f'character_id IS {i}'
    print(amt(num_items))

# Here is a better way to get the information... but I don't understand this
# as well.
count_items = 'SELECT character_id, count(character_id)' +
    'FROM charactercreator_character_inventory GROUP BY character_id'
a = curs.execute(count_items)
print(curs.execute(count_items).fetchall())

count_items = 'SELECT character_id, item_id, count(character_id)' +
    'FROM charactercreator_character_inventory GROUP BY character_id'
# You will notice that the second value in the tuples matches
# the values in the first output

# for i in range(1,20):
#     num_items = f'SELECT * FROM charactercreator_character_inventory WHERE character_id IS {i}'
#     sub = curs.execute()
#to get the names of the tables
# SELECT name FROM sqlite_master WHERE type = 'table'
