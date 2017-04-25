from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import hashlib, datetime, pprint
from dateutil import parser as dateparse

#start up flask app and restful api
app = Flask(__name__)
api = Api(app)

#create client to running instance, then set up database and log collection
client = MongoClient('localhost', 27017)
db = client.logging_database
logs = db.logs


#start up request parser
parser = reqparse.RequestParser()
parser.add_argument('uid')
parser.add_argument('date')
parser.add_argument('name')
parser.add_argument('md5checksum')



class Posting(Resource):
	def post(self):
		#grab name and checksum from json
		parser.replace_argument('uid', location='json', required=True, help="uid required for this request")
		parser.replace_argument('date', location='json', required=True, help="date required for this request")
		parser.replace_argument('name', location='json', required=True, help="name required for this request")
		parser.replace_argument('md5checksum', location='json', required=True, help="md5checksum required for this request")
		payload = parser.parse_args()
#		pprint.pprint(payload)
		# Generate checksum
		m = hashlib.md5()
		StringtoChecksum = '''{"date": "%(date)s", "uid": "%(uid)s", "name": "%(name)s"}''' %{'date': payload['date'], 'uid':payload['uid'], 'name': payload['name']}
		m.update(StringtoChecksum)
		# Verify checksums equal
		if payload['md5checksum'].lower() == m.hexdigest().lower():
			#convert given date format to datetime.datetime
			newdate = dateparse.parse(payload['date'])
			#create dictonary/doc
			data = {"uid": payload['uid'],
					"name": payload['name'],
					"date": newdate,
					"md5checksum": payload['md5checksum']}
#			pprint.pprint(data)		
			# insert doc into logs collection
			post_id = logs.insert_one(data).inserted_id
			return "Successfully inserted with post_id %s"%post_id
		else:
			#if checksums arent equal
			return "Error 400, bad checksum"


class Getting(Resource):
	def get(self):
		parser.replace_argument('uid', required=True, help="uid required for this operation")
		parser.replace_argument('date', required=True, help="date required for this operation")
		parser.replace_argument('name', required=False)
		parser.replace_argument('md5checksum', required=False)
		args = parser.parse_args()
		uid = args['uid']
		#convert datetime to start/end times
		d = dateparse.parse(args['date'])
		daystart = datetime.datetime(d.year,d.month,d.day)
		nextdaystart = daystart + datetime.timedelta(days=1)

		#run check on database for documents that have date within range:
			#daystart <= date < nextdaystart
			#AND that have the requested uid
		numberoflogs = logs.count({ "$and": [{"date": {"$gte": daystart}}, {"date": {"$lt": nextdaystart}}, {"uid": {"$eq": uid}}]})
		
		return numberoflogs


#class Checking(Resource):
#	def get(self):
#		cursor = logs.find({})
#		x = 0
#		for doc in cursor:
#			pprint.pprint(doc)
#			x = x + 1
#		return x


# First endpoint, for receiving POSTs
api.add_resource(Posting, '/post')

# Second endpoint, for GET requests
api.add_resource(Getting, '/get')

# Third Endpoint, for verifying post writes correctly to database
#api.add_resource(Checking, '/check')

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)