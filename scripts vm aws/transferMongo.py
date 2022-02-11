import json
import pymongo
import pandas as pd
import os

client = pymongo.MongoClient("mongodb+srv://bigdata:bigdata@rbnbdata.v5j0v.mongodb.net/airbnb?retryWrites=true&w=majority")
db = client.airbnb
collec = db['predict']
dftojson = pd.read_csv('dataPredict.csv')
dftojson.to_json('data.json')
data = json.load(open('data.json'))
x = collec.insert_one(dftojson)