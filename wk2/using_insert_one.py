import pymongo
import sys

# establish a connection to the network
connection = pymongo.MongoClient("mongodb://localhost")

def insert():

	# get a handle to the school database
	db = connection.school
	people = db.people

	print 'insert reporting for duty'

	lior = {"name": "Lior Shahverdi", "company":"ListStuff",
			"interests": ['standup', 'coding', 'eating']}
	andrew = {"_id":"erlichson", "name": "Andrew Erlichson", "company": "10gen",
				"interests": ['running', 'cycling', 'photography']}
	try:
		people.insert_one(lior)
		people.insert_one(andrew)
	except Exception as e:
		print 'Unexpected error:', type(e), e

	print lior
	print andrew

insert()

# causes an error when runs 2nd time - Duplicate key error
# lior is there twice, andrew is there once