from database import connect_db

db = connect_db()

# Collection for storing interview interactions
interview_collection = db["interviews"]

def save_interaction(user_question, ai_response):
    """
    Saves a conversation between user and AI in MongoDB.
    """
    interview_collection.insert_one({
        "question": user_question,
        "response": ai_response
    })

def get_all_interactions():
    """
    Retrieves all stored interactions from MongoDB.
    """
    return list(interview_collection.find({}, {"_id": 0}))  # Exclude MongoDB's `_id`
