


import os 
import telebot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("Not token bot")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def handler_start(message):
    bot.send_message(message.chat.id, "Здорова Братан, как дела? Как сам....")

print("start bot")
bot.polling(none_stop=True)
