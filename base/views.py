import pymongo
from django.shortcuts import render

# Create your views here.
client = pymongo.MongoClient("mongodb+srv://admin:1234@cluster0.tettcne.mongodb.net/?retryWrites=true&w=majority")
mydb = client['sample_analytics']
mycol = mydb['customers']

x = mycol.find_one()

print(x)
