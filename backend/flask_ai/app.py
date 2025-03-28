from flask import Flask
from flask_cors import CORS
from routes import ai_blueprint
from database import connect_db

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
db = connect_db()

# Register routes
app.register_blueprint(ai_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
