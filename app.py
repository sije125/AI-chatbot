from flask import Flask, render_template, request, jsonify
from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-15-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Store conversation history (in-memory for now)
conversation_history = []

if not conversation_history:
    conversation_history.append({
        "role": "system",
        "content": "You are a helpful AI assistant. Be friendly, concise, and informative."
    })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Add user message to history
    conversation_history.append({
        "role": "user",
        "content": user_message
    })
    
    # Call Azure OpenAI
    try:
        response = client.chat.completions.create(
            model=os.getenv("DEPLOYMENT_NAME"),
            messages=conversation_history,
            max_tokens=800,
            temperature=0.7
        )
        
        # Get assistant's response
        assistant_message = response.choices[0].message.content
        
        # Add to history
        conversation_history.append({
            "role": "assistant",
            "content": assistant_message
        })
        
        return jsonify({
            'response': assistant_message
        })
    
    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 500

@app.route('/reset', methods=['POST'])
def reset():
    global conversation_history
    conversation_history = []
    return jsonify({'status': 'reset'})

if __name__ == '__main__':
    app.run(debug=True)