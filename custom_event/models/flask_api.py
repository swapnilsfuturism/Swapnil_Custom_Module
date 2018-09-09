from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
from flask.ext.jsonpify import jsonify
import psycopg2
import sys
from datetime import datetime

"""
sudo pip install flask flask-jsonpify flask-restful
sudo pip3 install flask flask-jsonpify flask-restful

"""


app = Flask(__name__)
api = Api(app)

host = 'localhost'  #database host
user = 'admin'      #database user 
password = 'admin'  #database user password
database = 'demo'   #database name


con = psycopg2.connect(host=host, password=password, database=database, user=user)
cur = con.cursor()

class Employees_data(Resource):
    def get(self, employee_id):
        query = cur.execute("select * from res_partner where id =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)
        

api.add_resource(Employees_data, '/customer/<employee_id>') # Route_3


if __name__ == '__main__':
    app.run(port='8069')