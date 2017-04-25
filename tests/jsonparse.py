from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
#from pymongo import MongoClient
import hashlib, datetime, pprint
from dateutil import parser


app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('uid', required=True)
parser.add_argument('name', required=True)



#class Getting(Resource):
#	def get(self):
#		args = parser.parse_args()
#		print(args)
#		return 

class Posting(Resource):
	def post(self):
		args = parser.parse_args()
		print(args['name'])
		return args


#POST endpoint
api.add_resource(Posting, '/post')
#GET endpoint
#api.add_resource(Getting, '/get')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)