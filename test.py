import server
from server import *
import unittest
import json
import bcrypt
import base64
from pymongo import MongoClient
from random import  randint
from randomUser import Create_user
from randomUser import create_trip
import pdb
from basicauth import encode

class TripPlannerTestCase(unittest.TestCase):



    def setUp(self):

      self.app = server.app.test_client()
      # Run app in testing mode to retrieve exceptions and stack traces
      server.app.config['TESTING'] = True

      mongo = MongoClient('localhost', 27017)
      global db

      # Reduce encryption workloads for tests
      server.app.bcrypt_rounds = 4

      db = mongo.trip_planner_test
      server.app.db = db

      # db.drop_collection('users')
      # db.drop_collection('trips')







if __name__ == '__main__':
    unittest.main()
    tripTest = TripPlannerTestCase
    
