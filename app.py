"""
GLWIS Academic Bot - Flask Web Interface
Run this to access the bot via web browser at http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

try:
    from glwis_bot_simple import GLWISAcademicBot
except ImportError as e:
    print(f"Error: Could not import bot: {e}")
    GLWISAcademicBot = None

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

# Initialize bot
try:
    if GLWISAcademicBot is None:
        raise ImportError("GLWISAcademicBot not available")
    bot = GLWISAcademicBot()
    bot_ready = True
except Exception as e:
    print(f"Warning: Could not initialize bot: {e}")
    bot_ready = False
    bot = None

# Store conversation history
conversation_history = []

@app.route('/')
def index():
    """Main chat page"""
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """API endpoint for chat"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        if not bot_ready or bot is None:
            return jsonify({'error': 'Bot not initialized. Check API key in .env'}), 500
        
        # Get bot response
        bot_response = bot.answer_question(user_message)
        
        if not bot_response:
            bot_response = "Sorry, I encountered an error. Please try again."
        
        # Store in history
        conversation_history.append({
            'timestamp': datetime.now().isoformat(),
            'user': user_message,
            'bot': bot_response
        })
        
        return jsonify({
            'success': True,
            'response': bot_response,
            'history_count': len(conversation_history)
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    return jsonify({
        'history': conversation_history,
        'total': len(conversation_history)
    })

@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear conversation history"""
    global conversation_history
    conversation_history = []
    return jsonify({'success': True, 'message': 'History cleared'})

@app.route('/api/status', methods=['GET'])
def status():
    """Get bot status"""
    return jsonify({
        'status': 'ready' if bot_ready else 'error',
        'message': 'Bot is ready' if bot_ready else 'Bot initialization failed',
        'api_key_set': bool(os.getenv('OPENAI_API_KEY'))
    })

@app.route('/api/sample-questions', methods=['GET'])
def sample_questions():
    """Get sample questions"""
    questions = [
        "Where is GLWIS located?",
        "How much is the admission fee?",
        "What is the fee structure?",
        "What facilities are available?",
        "What extracurricular activities are offered?",
        "Does GLWIS have boarding?",
        "How can I contact the school?",
        "How is discipline handled?",
        "Are there sibling discounts?",
        "What is the student-teacher ratio?"
    ]
    return jsonify({'questions': questions})

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🎓 GLWIS ACADEMIC BOT - WEB INTERFACE")
    print("="*60)
    print("\n🌐 Web server starting...")
    print("📍 Open your browser and go to: http://localhost:5000")
    print("\n✅ Bot Status: " + ("Ready" if bot_ready else "ERROR - Check API key"))
    print("="*60 + "\n")
    
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        use_reloader=False  # Prevent double initialization
    )
