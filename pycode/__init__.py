from flask import Flask
import markdown
import os
from flask import g
import shelve
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = shelve.open('home_auto.db')
	return db

@app.teardown_appcontext
def teardown_db(exception):
	db = getattr(g, '_database', None)
	if db is not None:
		db.close()

@app.route("/")
def index():
	with open(os.path.dirname(app.root_path) + '/README.md','r') as readme_md:
		content = readme_md.read()
		return markdown.markdown(content)


class DeviceList(Resource):
	def get(self):
		db=get_db()
		data=[]
		for key in list(db.keys()):
			data.append(db[key])
		return {'status': 'success', 'data': data }, 200

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('identifier', type=str, required=True)
		parser.add_argument('description', type=str, required=True)
		parser.add_argument('type', type=str, required=True)
		parser.add_argument('address', type=str, required=True)
		args = parser.parse_args()
		db=get_db()
		db[args['identifier']]=args
		return {'status': 'success', 'data': args}, 201

class Device(Resource):
	def get(self, identifier):
		db=get_db()
		if identifier in list(db.keys()):
			return {'status':'success', 'data':db[identifier]}, 200
		else:
			return {'status':'Device not found in collection', 'data':{}}, 404
	def delete(self, identifier):
		db=get_db()
		if identifier in list(db.keys()):
			del db[identifier]
			return {'status':'success','data':{}}, 204
		else:
			return {'status':'Device not found in collection', 'data':{}}, 404

api.add_resource(DeviceList, '/devices')
api.add_resource(Device, '/device/<string:identifier>')