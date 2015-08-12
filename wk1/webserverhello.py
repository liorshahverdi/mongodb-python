from bottle import route, run, template
import pymongo

# this is the handler for the default path of the web server

@route('/')
def index():
	# connect to mongodb
	connection = pymongo.MongoClient('localhost', 27017)

	# attach to test database
	db = connection.test

	# get handle for names collection
	name = db.names

	# find a single document
	item = name.find_one()

	return '<b> Hello %s!</b>' % item['name']

run(host='localhost', port=8000)