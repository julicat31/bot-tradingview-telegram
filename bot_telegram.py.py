import requests
from flask import Flask, request

app = Flask(__name__)

# === CONFIGURA TUS DATOS AQUÍ ===
TOKEN = "7809226174:AAHsozxU9DVP2XyWyvKL17U-5yrwBwaasnA"       # Reemplaza con tu token de BotFather
CHAT_ID = "1347398020"          # Reemplaza con tu ID de usuario

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = f"📈 Señal recibida:\n\n🧠 Acción: {data['action']}\n📊 Par: {data['symbol']}\n💰 Precio: {data['price']}"
    send_message(message)
    return 'ok'

def send_message(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=payload)

app.run(host='0.0.0.0', port=5000)
