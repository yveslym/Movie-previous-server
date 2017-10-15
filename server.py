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
app.db = mongo.movie-preview
rounds = app.bcrypt_rounds = 12
api = Api(app)


class User(Resource):
    def __init__(self):
        first_name = ""
        last_name = ""
        email = ""
        password = ""
        user_name = ""
        movie_id = []
# function to authentificate user
# check if the email and password provided is the same in the db
    def user_auth(func):
        def wrapper(*args,**kwargs):
            auth_code = request.headers['authorization']
            email,password = decode(auth_code)
            user_dict = app.db.users.find_one({'email':email})
            if user_dict is not None:
                encoded_pw = password.encode('utf-8')
                if bcrypt.hashpw(encoded_pw,user_dict['password']) == user_dict['password']:
                    return func(*args, **kwargs)
                else:
                    return ({'error':'email or password incorect'},401,None)
            else:
                return({'error':'user does not exist'},400,None)
    return wrapper

    # function to ad user in the data base
    # check if the user fill out all field and add
    def post(self):
        json_data = request.json
        first_name = json_data.get["first_name"]
        last_name = json_data.get("last_name")
        email = json_data.get("email")
        password = json_data.get("password")

        if first_name is not None and last_name is not None and email is not None and password is not None:
            user_col = app.db.users
            encoded_password = password.encode("uft-8")
            ashed = bcrypt.hashpw(encoded_password,bcrypt.gensalt(rounds))
            user_dict = json_data
            user_dict['password'] = ashed
            user_col.insert_one(user_dict)
            return (json_data,200,None)
        else:
            return({'error':'fill out all field'},400,None)

    #function to get user from the database
    #check first if the user auth is correct the get the user
    @user_auth
    def get(self):

        auth_code = request.headers['authorization']
        email,password = decode(auth_code)
        user_dict = app.db.users.find_one({'email':'password'})
        user_dict.pop('password')
        return(user_dict,200,None)

    @user_auth
    def delete (self):


















api.add_resource(User, '/users')
api.add_resource(Trip, '/movies')


#  Custom JSON serializer for flask_restful
@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder().encode(data), code)
    resp.headers.extend(headers or {})
    return resp

if __name__ == '__main__':

    # Turn this on in debug mode to get detailled information about request
    # related exceptions: http://flask.pocoo.org/docs/0.10/config/
    app.config['TRAP_BAD_REQUEST_ERRORS'] = True
    app.run(debug=True)
