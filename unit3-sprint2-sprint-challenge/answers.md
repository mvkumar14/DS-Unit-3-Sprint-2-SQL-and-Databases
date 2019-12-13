Part 1:
[('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

#1:
[(3,)]

#2:
[(2,)]

#3:
[(2,)]

Part 2:
#1:
[('C�te de Blaye', 263.5), ('Th�ringer Rostbratwurst', 123.79), ('Mishi Kobe Niku', 97), ("Sir Rodney's Marmalade", 81), ('Carnarvon Tigers', 62.5), ('Raclette Courdavault', 55), ('Manjimup Dried Apples', 53), ('Tarte au sucre', 49.3), ('Ipoh Coffee', 46), ('R�ssle Sauerkraut', 45.6)]

#2:
[(37.22222222222222,)]

Part 3:
#1:
[('Exotic Liquids', 'C�te de Blaye', 263.5), ('New Orleans Cajun Delights', 'C�te de Blaye', 263.5), ("Grandma Kelly's Homestead", 'C�te de Blaye', 263.5), ('Tokyo Traders', 'C�te de Blaye', 263.5), ("Cooperativa de Quesos 'Las Cabras'", 'C�te de Blaye', 263.5), ("Mayumi's", 'C�te de Blaye', 263.5), ('Pavlova, Ltd.', 'C�te de Blaye', 263.5), ('Specialty Biscuits, Ltd.', 'C�te de Blaye', 263.5), ('PB Kn�ckebr�d AB', 'C�te de Blaye', 263.5), ('Refrescos Americanas LTDA', 'C�te de Blaye', 263.5)]

#2:
[('Confections', 13)]


Part 4

- In the Northwind database, what is the type of relationship between the `Employee` and `Territory` tables?
    It is a many to many relationship. They are connected through the intermediary table employee territories
- What is a situation where a document store (like MongoDB) is  appropriate, and what is a situation where it is not appropriate?
    It is appropriate when you have a huge amount of data, and when
    your data is unstructured, or when its structure cannot be captured by a relational architecture. It is also useful when you want to parallelize the functions that you apply on your database, or when all of the expected functions on your database will be parallel, because the distributed system is suited to parallel computing. Additionally a document store might be useful in the prototyping stages of a project where the exact schema of a database might not be known. It is not appropriate when you have small amounts of data, and the relationship between the data is known, or easily captured through a relational database. A document store also doesn't have ACID guarantees like a traditional SQL database. If those guarantees are a design requirement due to the nature of the information being stored, then document stores are not appropriate.
- What is "NewSQL", and what is it trying to achieve?
    NewSQL is a system that tries to acheive the best parts of NoSQL and SQL. It tries to combine the ACID guarantees with the  scalability of NoSQL.
