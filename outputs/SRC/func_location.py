import pandas as pd
from pymongo import MongoClient
import requests
dbName = "mongoProject"
mongodbURL = f"mongodb://localhost/{dbName}"
client = MongoClient(mongodbURL, connectTimeoutMS=2000, serverSelectionTimeoutMS=2000)
client= MongoClient("mongodb://localhost/mongoProject")
db = client.get_database()
client = MongoClient()


def geocode(address):
    res = requests.get(f"https://geocode.xyz/{address}", params={"json":1})
    data = res.json()
    return {
"type":"Point",
"coordinates":[float(data["longt" ]),float(data["latt"])]
}

def geoQueryNear(point,radius=10000):
    return {
        "geopoint":{
            "$near": {
                "$geometry": point,
                "$maxDistance": radius,
                "$minDistance": 0
            }
        }
    }