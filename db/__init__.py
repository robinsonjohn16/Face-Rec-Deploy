from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

client = MongoClient(os.getenv("DATABASE_URL"))
# client = MongoClient(os.getenv("DATABASE_URL", 27017))
# client = MongoClient(os)
print(client)
