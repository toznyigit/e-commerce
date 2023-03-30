import pymongo, json

class Connector:
    client = pymongo.MongoClient("mongodb+srv://tozanyigit:JKZa42zqmvXoM89V@cluster0.ngbxgkp.mongodb.net/?retryWrites=true&w=majority")

class UserDB(Connector):
    
    def __init__(self):
        super().__init__()
        self.db = self.client.Auth
        self.col = self.db.Users

    def create(self, **kwargs):
        self.col.insert_one(kwargs)

    def read(self, **kwargs):
        return self.col.find_one(kwargs)

    def update(self, **kwargs):
        pass

    def delete(self, **kwargs):
        self.col.delete_one(kwargs)

    def readAll(self):
        return self.col.find({})

class ItemDB(Connector):
    pass