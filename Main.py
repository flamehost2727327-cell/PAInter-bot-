import telebot
import os
from flask import Flask, request

TOKEN = os.getenv("8594840158:AAECFiMWhdWod-cTiVynyb1KUDCG5St1Wf0")
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я живой 🔥")

@app.route(f'/{TOKEN}', methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route('/')
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f'https://your-render-url.onrender.com/{TOKEN}')
    return 'Bot started!', 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
