import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv() # .env 파일을 읽어온다
# .env 파일에서 MONGODB_URI 해당하는 값을 가져와서, MongoClient가 식별할 수 있게 한다.
db_connect = MongoClient(os.environ.get("MONGODB_URI")) 
# db에서 local 컬렉션을 들고온다.
db = db_connect.local