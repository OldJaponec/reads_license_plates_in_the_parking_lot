from pymongo import MongoClient
import datetime

from setting import password, connection_string, database_name, collection_name


# cut link to paste password
connection = connection_string.split('<password>')

# paste the password
cluster = MongoClient(connection[0] + password + connection[1])

# specify database and collection
db = cluster[database_name]
collection = db[collection_name]


def insert_base(plate, answer):
	'''
	The function to insert license plate, response and time data into the database
	'''
	# add data to dictionary
	post = {
	'plate': plate,
	'answer': answer,
	'data': datetime.datetime.utcnow()
	}

	# add dictionary to database
	collection.insert_one(post)