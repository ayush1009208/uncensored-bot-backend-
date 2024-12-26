from flask import Flask, request, jsonify
from langchain_ollama import OllamaLLM
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Get the Ollama model name from environment variable or use a default
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "dolphin-mistral")

try:
    llm = OllamaLLM(model=OLLAMA_MODEL)
    print(f"Using Ollama model: {OLLAMA_MODEL}")
except Exception as e:
    print(f"Error initializing Ollama with model {OLLAMA_MODEL}: {e}")
    llm = None

@app.route('/chat', methods=['POST'])
def chat():
    if llm is None:
        return jsonify({'error': f'Ollama model "{OLLAMA_MODEL}" is not initialized. Check server logs and ensure Ollama is running with this model.'}), 500

    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided in JSON'}), 400

        user_message = data['message']
        response = llm(user_message)
        return jsonify({'response': response}), 200

    except Exception as e:
        print(f"Error processing chat request: {e}")
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)