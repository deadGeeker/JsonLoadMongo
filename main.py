import json
import os
from pymongo import MongoClient


url = os.getcwd()
print(url)
json_data_list = []
file_name_list = os.listdir(url)

for file_name in file_name_list:
    if file_name.endswith('.json'):
        with open(file_name) as f:
            json_data_list.append(json.load(f))

client = MongoClient(host='localhost')
db = client.challenge
db.file.insert_many(json_data_list)
print(list(db.file.find({})))
