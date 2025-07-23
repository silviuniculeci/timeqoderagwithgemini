import os
from datetime import datetime
import uuid

from flask import Flask, send_file, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from src.ai_assistant import AIAssistant

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/chat_history.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define ChatSession Model
class ChatSession(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.isoformat()
        }

# Define ChatMessage Model
class ChatMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(36), db.ForeignKey('chat_session.id'), nullable=False)
    prompt = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    session = db.relationship('ChatSession', backref=db.backref('messages', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'prompt': self.prompt,
            'response': self.response,
            'timestamp': self.timestamp.isoformat()
        }

ai_assistant = AIAssistant(operators_path='knowledge_base')

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/new-chat", methods=['POST'])
def new_chat():
    new_session = ChatSession(title="New Chat") # Temporary title, will be updated with first message
    db.session.add(new_session)
    db.session.commit()
    print(f"--- Created new chat session: {new_session.id} ---")
    return jsonify({"session_id": new_session.id, "title": new_session.title})

@app.route("/generate-logic", methods=['POST'])
def generate_logic():
    try:
        data = request.json
        prompt = data.get('prompt')
        session_id = data.get('session_id')

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400
        if not session_id:
            return jsonify({"error": "Session ID is required"}), 400

        # Retrieve chat history for context
        chat_messages = ChatMessage.query.filter_by(session_id=session_id).order_by(ChatMessage.timestamp.asc()).all()
        history = []
        for msg in chat_messages:
            history.append({"role": "user", "parts": [msg.prompt]})
            history.append({"role": "model", "parts": [msg.response]})

        generated_logic = ai_assistant.generate_logic(prompt, history)
        
        # Save chat to database
        new_message = ChatMessage(session_id=session_id, prompt=prompt, response=generated_logic['logic'])
        db.session.add(new_message)
        db.session.commit()
        print(f"--- Saved message to session {session_id}: Prompt='{prompt}', Response='{generated_logic['logic']}' ---")

        # Update session title with first message if it's a new session
        session = ChatSession.query.get(session_id)
        if session and session.title == "New Chat":
            session.title = prompt[:50] + "..." if len(prompt) > 50 else prompt
            db.session.commit()
            print(f"--- Updated session {session_id} title to: {session.title} ---")

        return jsonify(generated_logic)
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route("/chat-history/<session_id>", methods=['GET'])
def chat_history(session_id):
    print(f"--- /chat-history/{session_id} endpoint hit ---")
    messages = ChatMessage.query.filter_by(session_id=session_id).order_by(ChatMessage.timestamp.asc()).all()
    print(f"--- Retrieved {len(messages)} messages for session {session_id} from database ---")
    return jsonify([msg.to_dict() for msg in messages])

@app.route("/chat-sessions", methods=['GET'])
def chat_sessions():
    print("--- /chat-sessions endpoint hit ---")
    sessions = ChatSession.query.order_by(ChatSession.created_at.desc()).all()
    print(f"--- Retrieved {len(sessions)} chat sessions ---")
    return jsonify([s.to_dict() for s in sessions])

# This function will be called once when the application starts
# It ensures the database tables are created before any requests are handled.
with app.app_context():
    if os.path.exists('chat_history.db'):
        os.remove('chat_history.db')
        print("Removed existing chat_history.db for a clean start.")
    db.create_all()
    print("Database tables created.")

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()