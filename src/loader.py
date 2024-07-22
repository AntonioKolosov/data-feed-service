# Mongo
from sqlite3 import Cursor
from pymongo.mongo_client import MongoClient

from src.config import mongo_uri, mongo_database, data_collection


def load_content(name: str) -> dict:
    """Load content from database"""

    uri = mongo_uri
    print(uri)

    with MongoClient(uri) as client:
        db = client[mongo_database]
        collection = db[data_collection]
        cursor: Cursor = collection.find({"name": name})  # type: ignore
        doc = list(cursor)
        return doc[0]  # type: ignore
