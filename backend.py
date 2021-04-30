from flask import Flask
from bson.objectid import ObjectId
from bson.json_util import dumps
import pymongo


client = pymongo.MongoClient('mongodb://db-service:27017')
mydb = client['MYDATA2']
ques_collection=mydb.question
ans_collection=mydb.answer

