from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
import hashlib
import json

app = Flask(__name__)
api = Api(app)
#mongo = PyMongo(app)

#parser = reqparse.RequestParser()
#parser.add_argument('uid', type=int, help='uid must be an integer')
#parser.add_argument('name')
#parser.add_argument('date')
#parser.add_argument('md5checksum')


class Posting(Resource):
	def post(self):
		payload = request.get_json(force=True)
		# verify checksum
		m = hashlib.md5()
		StringtoChecksum = '''{"date": "%(date)s", "uid": "%(uid)s", "name": "%(name)s"}''' %{'date': payload['date'], 'uid':payload['uid'], 'name': payload['name']}
		m.update(StringtoChecksum)
#		print(StringtoChecksum)
#		print("""{"date": "2015-05-12T14:36:00.451765", "uid": "1", "name": "John Doe"}""")
#		print(m.hexdigest().lower())
		print(payload['md5checksum'].lower())
		if payload['md5checksum'].lower() == m.hexdigest().lower():
			return "this is great"
		else:
			return "nope"






#	def get(self, uid, date):


# First endpoint, for receiving POSTs
api.add_resource(Posting, '/post')



# for checking connection. remove in final submission
@app.route("/checkConn")
def hello():
	return "Hello World! noDB.py \n"


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)