#!/usr/bin/env python3
"""Write a Python script that provides some stats about Nginx
logs stored in MongoDB:"""
from pymongo import MongoClient
if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx
    print(collection.count_documents({}), "logs")
    print("\tmethod GET:",collection.count_documents({"method": "GET"}))
    print("\tmethod POST:",collection.count_documents({"method": "POST"}))
    print("\tmethod PUT:",collection.count_documents({"method": "PUT"}))
    print("\tmethod PATCH:",collection.count_documents({"method": "PATCH"}))
    print("\tmethod DELETE:",collection.count_documents({"method": "DELETE"}))
    print(collection.count_documents({"path": "/status"}),"status check")