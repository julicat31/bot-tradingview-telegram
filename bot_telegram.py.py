import os
import requests
from flask import Flask, request

app = Flask(__name__)

# Usa variables de entorno definidas en Render
TOKEN = os.getenv("7809226174:AAHsozxU9DVP2XyWyvKL17U-5yrwBwaasnA")
CHAT_ID = os.getenv("1347398020")

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = f"📈 Señal recibida:\n\n🧠 Acción: {data.get('action')}\n📊 Par: {data.get('symbol')}\n💰 Precio: {data.get('price')}"
    send_message(message)
    return 'ok'

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
  
