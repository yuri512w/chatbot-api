import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Defina sua chave da OpenAI
openai.api_key = "SUA_API_KEY_AQUI"

@app.route('/chat', methods=['POST'])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "A mensagem não pode estar vazia"}), 400

    # Usando o novo formato da API OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response.choices[0].message.content

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
