from flask import Flask
from flask_restful import Resource, Api
from flask_pymongo import PyMongo

app = Flask(__name__)
api = Api(app)
mongo = PyMongo(app)








# First endpoint, for receiving POSTs
# api.add_resource()


@app.route("/")
def hello():
	return "Hello World!"




if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)