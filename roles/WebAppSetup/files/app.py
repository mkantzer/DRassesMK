from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import hashlib, datetime, pprint

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

			post = {"uid": "%s"%payload['uid']
					"name": "%s"%payload['uid']
					"date": "%s"%payload['uid']
					"md5checksum": "%s"%payload['uid']
					}

			

			return "added to database"
		

		else:
			return "nope"

#this may need to be under a different class/resource
#	def get(self, uid, date):


# First endpoint, for receiving POSTs
api.add_resource(Posting, '/post')



# for checking connection. remove in final submission
#@app.route("/checkConn")
#def hello():
#	return "Hello World! noDB.py \n"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)