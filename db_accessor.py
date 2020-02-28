# coding:utf-8
from pymongo import MongoClient
import os
import json
import bson.objectid
import datetime


def json_handler(x):
    if isinstance(x, datetime.datetime):
        return x.isoformat()
    elif isinstance(x, bson.objectid.ObjectId):
        return str(x)
    else:
        raise TypeError(x)


class DBAccess():
    """
    mongo
    """

    def __init__(self, url="localhost", db="test", collection="test"):
        """
        """
        self.client = MongoClient(
            "mongodb://{}:{}@{}".format("root", "example", url))
        self.db = self.client[db]
        self.coll = self.db[collection]

    def insert(self, json, collection="test"):
        """

        """
        try:
            # insert one
            self.coll.insert_one(json)
            # insert many
            # coll.insert_many(json)
        except:
            pass

    def show_all(self):
        """

        """
        items = self.coll.find()
        return json.dumps(list(items), default=json_handler, ensure_ascii=False)

    def update(self, query, json):
        """
        updateを実行する．
        """
        items = self.coll.find_one_and_update(query, {"$set": json})

    def find(self, query, collection="test"):
        """
        """
        try:
            item = self.coll.find_one(query)
            del item["_id"]
            return json.dumps(item, ensure_ascii=False)
        except:
            return json.dumps({})

    def null_data(self, field="title"):
        """

        """
        try:
            l = list(self.coll.find({field: {"$exists": False}}))
        except:
            pass
        return l


if __name__ == "__main__":
    obj = DBAccess()
    from book_search_api import BookSearchAPI
    api = BookSearchAPI()
    data = api.get_json("9784295004806")
    print(data)
