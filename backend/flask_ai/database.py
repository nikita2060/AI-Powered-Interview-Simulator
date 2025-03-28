from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

def connect_db():
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client["ai_interview_db"]
    print("MongoDB Connected Successfully!")
    return db
