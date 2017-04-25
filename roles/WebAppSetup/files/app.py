from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import hashlib, datetime, pprint
from dateutil import parser as dateparse

app = Flask(__name__)
api = Api(app)

#create client to running instance
client = MongoClient('localhost', 27017)
#set up database
db = client.logging_database
#set up log collection
logs = db.logs


#set up request parser
parser = reqparse.RequestParser()
parser.add_argument('uid', required=True, help="uid required for this request")
parser.add_argument('date', required=True, help="uid required for this request")


class Posting(Resource):
	def post(self):
		#grab name and checksum from json
		parser.add_argument('name', location='json', required=True)
		parser.add_argument('md5checksum', location='json', required=True)
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


#this may need to be under a different class/resource
#	def get(self, uid, date):


# First endpoint, for receiving POSTs
api.add_resource(Posting, '/post')

# Second endpoint, for GET requests
#api.add_resource(Getting, '/get')



# for checking connection. remove in final submission
#@app.route("/checkConn")
#def hello():
#	return "Hello World! noDB.py \n"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)