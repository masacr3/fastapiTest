from pymongo import MongoClient
from cfg import settings

client = MongoClient(settings.MONGO_URI)
db = client[settings.MONGO_DB]
collection = db[settings.MONGO_TABLE_MEDICACION]