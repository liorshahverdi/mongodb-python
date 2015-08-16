import pymongo
import sys

# establish a connection to the network
connection = pymongo.MongoClient("mongodb://localhost")

def insert_many():
	# get a handle to the school database
	db = connection.school
	people = db.people
	print 'insert_many reporting for duty'
	andrew = {"_id": "erlichson", "name": "Andrew Erlichson", "company":"MongoDB",
				"interests": ['running', 'cycling', 'photography']}
	richard = {"name": "Richard Kreuter", "company": "MongoDB",
				"interests":['horses','skydiving','fencing']}
	people_to_insert = [andrew,richard]
	try:
		people.insert_many(people_to_insert, ordered=True)
		# In the line above, if our ordered  parameter were == false, if we kept
		# running our program repeatedly there would be 1 document for andrew and an additional
		# document for richard with a new value for id
		# This is because the ordered parameter guarantees whether or not to 
		# insert the documents in order, which would stop the inserts on an error
	except Exception as e:
		print 'Unexpected error', type(e), e

def print_people():
	# get a handle to the school database
	db = connection.school
	people = db.people

	cur = people.find({}, {'name': 1})
	for doc in cur:
		print doc

print "Before the insert_many, here are the people"
print_people()
insert_many()
print "\n\nAfter the insert_many, here are the people"
print_people()