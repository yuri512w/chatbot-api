import openai
import os
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Defina sua chave da OpenAI via variável de ambiente para segurança
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chatbot():
    """
    Interage com o chatbot usando a API OpenAI GPT
    ---
    tags:
      - Chatbot
    parameters:
      - name: message
        in: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Olá, como você está?"
    responses:
      200:
        description: Resposta do chatbot
        schema:
          type: object
          properties:
            response:
              type: string
              example: "Estou bem! Como posso te ajudar hoje?"
      400:
        description: Erro de solicitação inválida
    """
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "A mensagem não pode estar vazia"}), 400

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_reply = response["choices"][0]["message"]["content"]

    return jsonify({"response": bot_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
