import os
from dotenv import load_dotenv

load_dotenv()

mongo_uri = os.environ.get("MONGO_URI", "")
mongo_database = os.environ.get("MONGO_DATABASE", "")
data_collection = os.environ.get("DATA_COLLECTION", "")

print(f'mongo_uri - {mongo_uri}')
print(f'mongo_database - {mongo_database}')
print(f'data_collection - {data_collection}')
