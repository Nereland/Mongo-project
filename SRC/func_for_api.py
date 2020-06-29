import json
import os
import pandas as pd
import dotenv
from dotenv import load_dotenv
import requests
load_dotenv()
import numpy as np

def getfromgooglecloud(queryParams={}):
    url = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
    res = requests.get(url, params=queryParams)
    response = res.json()
    results = response["results"] 
    return results


def getQueryParams(lat,long,radius,sort,keyword):
    apiKey = os.getenv("GoogleToken")
    if not apiKey:
        raise ValueError("Please set up the GoogleToken env variable")
    return  {
    "location":lat + ","+ long,
    "radius":radius,
    "type":sort,
    "keyword":keyword,
    "key":f'{apiKey}'}


def toGetGeometry(data):
    infor = []
    for j in range(len(data)):
        info ={"name": data[j]["name"], 
               "latitude":data[j]["geometry"]["location"]["lat"], 
               "longitude": data[j]["geometry"]["location"]["lng"]}
        infor.append(info)
    return infor



def transformToGeoPoint(s):
    if np.isnan(s.latitude) or np.isnan(s.longitude):
        return None
    return {
        "type":"Point",
        "coordinates":[s.longitude, s.latitude]
    }
