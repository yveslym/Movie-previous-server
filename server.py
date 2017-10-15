from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
from utils.mongo_json_encoder import JSONEncoder
from bson.objectid import ObjectId
import bcrypt
from mongoengine import *
import pdb
import uuid
from socket import *
from basicauth import decode

sock=socket()
sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.trip_planner_test
rounds = app.bcrypt_rounds = 12
api = Api(app)










if __name__ == '__main__':

    # Turn this on in debug mode to get detailled information about request
    # related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
