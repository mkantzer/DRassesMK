from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
import hashlib, datetime, pprint
from dateutil import parser

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()


thingy = {
	'1': {'name': 'Mike'},
	'2': {'name': 'Jack'}
}


class Getting(Resource):
	def get(self):
		parser.add_argument('uid', required=True, help='uid required')
		parser.add_argument('fruit')
		args = parser.parse_args()
		print(args)
		return thingy[args['uid']]



#get endpoint
api.add_resource(Getting, '/get')



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)