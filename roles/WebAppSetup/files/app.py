from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import hashlib, datetime, pprint
from dateutil import parser

app = Flask(__name__)
api = Api(app)

#create client to running instance
client = MongoClient('localhost', 27017)
#set up database
db = client.logging_database
#set up log collection
logs = db.logs



class Posting(Resource):
	def post(self):
		payload = request.get_json(force=True)
		# Generate checksum
		m = hashlib.md5()
		StringtoChecksum = '''{"date": "%(date)s", "uid": "%(uid)s", "name": "%(name)s"}''' %{'date': payload['date'], 'uid':payload['uid'], 'name': payload['name']}
		m.update(StringtoChecksum)
		# Verify checksums equal
		if payload['md5checksum'].lower() == m.hexdigest().lower():
			#convert given date format to datetime.datetime
			newdate = parser.parse(payload['date'])
			#create dictonary/doc
			data = {"uid": payload['uid'],
					"name": payload['name'],
					"date": newdate,
					"md5checksum": payload['md5checksum']}
#			pprint.pprint(data)		
			post_id = logs.insert_one(data).inserted_id
			return "Successfully inserted with post_id %s"%post_id
		else:
			#if checksums arent equal
			return "Error 400, bad checksum"

#class Getting(Resource):
#	def get(self, ):


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