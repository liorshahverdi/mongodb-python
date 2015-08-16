# Replaces the whole document rather than just a single attribute
import pymongo
import datetime
import sys

# establish a connection to the db
connection = pymongo.MongoClient('mongodb://localhost')

#removes all review dates
def remove_all_review_dates():
	print '\nremoving all review dates'

	# get a handle to the school db
	db = connection.school
	scores = db.scores
	try:
		result = scores.update_many({'review_date': {'$exists': True}},
									{'$unset': {'review_date':1}})
		print 'Matched this number of docs: ', result.matched_count
	except Exception as e:
		raise

def add_review_date_using_replace_one(student_id):
	# get a handle to the school db
	db = connection.school
	scores = db.scores

	try:
		# get the doc
		score = scores.find_one({'student_id':student_id, 'type': 'homework'})
		print 'before: ', score

		# add a review date
		score['review_date'] = datetime.datetime.utcnow()

		# update the record with replace_one
		record_id = score['_id']
		scores.replace_one({'_id': record_id}, score)
		score = scores.find_one({'_id': record_id})
		print 'after: ', score

	except Exception as e:
		print 'Unexpected error:', type(e), e
		raise

remove_all_review_dates()
add_review_date_using_replace_one(1)