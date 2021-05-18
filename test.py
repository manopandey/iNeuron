import pymongo

client = pymongo.MongoClient("mongodb+srv://mongouser:mongopassword@ineuron.nh9in.mongodb.net/myFirstDatabase?retryWrites=true&w=majority",ssl=True,ssl_cert_reqs='CERT_NONE')
database = client["database"]
collection = database["test"]
record = {'company':'iNeuron',
            'Name':'Mano',
            'Age':'30'}

# collection.insert_one(record)

list_of_records_user_defined_id = [
    {"_id": "1",
    "companyName": "iNeuron",
    "Faculty": "Sudhanshu Kumar"},
    {"_id": "2",
    "companyName": "iNeuron",
    "Faculty": "Virat Sagar"},
]

collection.insert_many(list_of_records_user_defined_id)