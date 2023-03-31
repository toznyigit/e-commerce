import pymongo, json
from bson import json_util
class Connector:
    client = pymongo.MongoClient("mongodb+srv://tozanyigit:JKZa42zqmvXoM89V@cluster0.ngbxgkp.mongodb.net/?retryWrites=true&w=majority")
    db = client.E_Commerce

    def __init__(self):
        self.col = None

    def create(self, **kwargs):
        self.col.insert_one(kwargs)

    def read(self, **kwargs):
        return self.col.find_one(kwargs)

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        self.col.delete_one(kwargs)

class UserDB(Connector):
    
    def __init__(self):
        super().__init__()
        self.col = self.db.Users

    def readAll(self):
        return self.col.find({})

class ItemDB(Connector):
    def __init__(self):
        super().__init__()
        self.col = self.db.Items

    def readAll(self, **kwargs):
        cursor = self.col.find({"type": kwargs['category']})
        json_data = json.loads(json_util.dumps(cursor))
        return json_data