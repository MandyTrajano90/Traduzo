from pymongo import MongoClient
import os

conection = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(conection)

db_client = os.environ.get('DB_NAME', 'test_db_traduzo')

db = client[db_client]
