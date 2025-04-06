from flask import Blueprint, request, jsonify
from ai_processing import generate_response
from database import connect_db

db = connect_db()
ai_blueprint = Blueprint("ai", __name__)

@ai_blueprint.route("/ask", methods=["POST"])
def ask_ai():
    data = request.json
    user_input = data.get("question")

    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    response = generate_response(user_input)

    # Save to MongoDB
    db.interviews.insert_one({"question": user_input, "response": response})
    
    return jsonify({"response": response})
