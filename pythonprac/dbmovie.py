from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:as123123@cluster0.nnsglfi.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})