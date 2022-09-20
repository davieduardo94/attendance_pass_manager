from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
load_dotenv()


class MongoCon():
    def __init__(self) -> None:
        self.conn = MongoClient("mongodb+srv://atd_mongo:"+environ["mongo_pass"]+"@sandbox.vjmhshf.mongodb.net/?retryWrites=true&w=majority")
    
    def make_db(self, db_name, coll_name):
        pass