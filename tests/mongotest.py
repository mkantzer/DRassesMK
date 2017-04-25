from flask import Flask
import pymongo
from pymongo import MongoClient
import datetime, pprint

# Create client to running instance
client = MongoClient('localhost', 27017)

#get a database:
db = client.test_database

#getting a collection:
collection = db.test_collection


#MongoDB data stored like JSON; PyMongo uses dictonaries to represent documents
#post = {"author": "Steve",
#		"test": "Look at Me!",
#		"tags": ["mongodb", "python", "pymongo"],
#		"date": datetime.datetime.utcnow()}

# To instert a doc into a collection:

posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#print(post_id)
#print()
print()
print()
print()

#view list of all collections
#print(db.collection_names(include_system_collections=False))


# you can use posts.inster_many(lots of posts) to insert several at once, but eh, not for now, I dont think I need that?

#Querrying for mor than one Document:
#use find() method; returns a Cursor instance, which we can iterate

#for post in posts.find({"author": "Steve"}):
#	pprint.pprint(post)


#however, for this, I dont actually need to retreive the full set of documents. 
# I only need a count!!!
print(posts.count())

print(posts.find({"author": "Steve"}).count())


#okay, so I'll be able to use uid/name for the request, but date is an issue
#range?

#from date, get start and end times
d = datetime.date.today()
m = datetime.datetime(d.year,d.month,d.day)
n = m + datetime.timedelta(days=1)
print(d)
print(m)
print(n)


#search for posts during or after first midnight, but only before second
#for post in posts.find( { "$and": [{"date": {"$gte": m}},{"date": {"$lt": n}}]}):
#	pprint.pprint(post)

#get count
print(posts.count( { "$and": [{"date": {"$gte": m}},{"date": {"$lt": n}}]}))
