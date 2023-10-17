from pymongo import MongoClient
from dotenv import load_dotenv
from os import environ
load_dotenv()


class MongoCon():
    uri = "mongodb+srv://atd_mongo:"+environ["mongo_pass"]+"@sandbox.vjmhshf.mongodb.net/?retryWrites=true&w=majority"

    def __init__(self) -> None:
        self.conn = MongoClient(self.uri)
        
    
    def make_db(self):
        self.db = self.conn.attendance_password
        collection = self.db.user_attendance
        return collection

test = MongoCon()