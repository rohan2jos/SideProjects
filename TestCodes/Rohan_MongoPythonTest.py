from pymongo import MongoClient

# create an instance of the MongoClient so that all the methods are accessible
client = MongoClient()

# establish a connection with the database
db = client.restaurants

result = db.restaurants.insert([
    {
        "address": "some address",
        "name": "some name"
    },
    {
        "address": "some address again",
        "name": "some name again"
    }
    ]
)