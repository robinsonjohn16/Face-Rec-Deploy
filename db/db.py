from dotenv import load_dotenv
import pymongo
import os
load_dotenv()

# dbUrl = os.getenv("DATABASE_URL")
# # app.config["MONGO_URI"] = os.getenv("DATABASE_URL").
# client = pymongo.MongoClient(dbUrl, 27017)

# dbName = os.getenv("DATABASE_NAME")
# db = client.dbName

client = pymongo.MongoClient('localhost', 27017)
db = client.user_login_system
