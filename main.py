from flask import Flask, request, jsonify
from openai import OpenAI
import os
from flask_cors import CORS

#pip install openai

app = Flask(__name__)
CORS(app)  # Habilita CORS para todos los orígenes

OPENAI_KEY = "xxxxxx"

client = OpenAI(
    organization='org-8AghacFhYbrLH96uY8obz0Z2',
    project='proj_IWuNJKJuCbFd4ZOh6IOldtkB',
    api_key=OPENAI_KEY
)

@app.route("/ask", methods=["POST"])
def ask_openai():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "El campo 'prompt' es requerido"}), 400

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return jsonify({"response": response.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

"""
curl -X POST http://localhost:5080/ask \
  -H "Content-Type: application/json" \
  -d '{"prompt": "¿Cuál es la diferencia entre IA y Machine Learning?"}'
"""

#python3 main.py
#python3 -m http.server 8000

if __name__ == "__main__":
    app.run(debug=True, port=5080)