import pymongo
import json
from bson import ObjectId

# connection string
mongo_url = "mongodb://localhost:27017"
client = pymongo.MongoClient(mongo_url)

# get the specific database from the db service
db = client.get_database("organikaCh23")





# create a class that knows how to parse ObjectId into json string
# because json.dumps can not handle ObjectId returned by the db
class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        
        return json.JSONEncoder.default(obj)




def json_parse(data):
    return JSONEncoder().encode(data)