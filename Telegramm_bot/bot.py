#Создаём телеграмм бота, учимся от простого к сложном!
#учимся создавать виртуальное окружение

"""python3 -m venv .venv
source .venv/bin/activate""" 
# pip install python-telegram-bot --upgrade


import telebot
import os 
from dotenv import load_dotenv


load_dotenv()

# me token bot 
BOT_TOKEN = os.getenv('BOT_TOKEN')
if BOT_TOKEN is None:
    raise ValueError('Ошибка: токен не найден в файле!')

bot = telebot.TeleBot(str(BOT_TOKEN))



# Команды / старт 

@bot.message_handler(commands = ['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я твой первый бот. Напиши мне что ни будь...')
    

#Ответ на любой текст
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f'Ты написал: {message.text}') 


# Запуск бота
bot.infinity_polling()












