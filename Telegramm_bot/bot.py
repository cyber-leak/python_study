# Создаём телеграмм бота, учимся от простого к сложном!
# учимся создавать виртуальное окружение

"""python3 -m venv .venv
source .venv/bin/activate"""
# pip install python-telegram-bot --upgrade


import os

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()

# me token bot
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("Ошибка: токен не найден в файле!")

bot = telebot.TeleBot(str(BOT_TOKEN))


# Команды / старт


@bot.message_handler(commands=["start"])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Привет!")
    btn2 = types.KeyboardButton("Пока")
    btn3 = types.KeyboardButton("Помощь")

    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выбери действие: ", reply_markup=markup)

    bot.reply_to(
        message,
        "Привет! Я твой первый бот. Напиши мне что ни будь...",
        reply_markup=markup,
    )


# Обработка кнопок


@bot.message_handler(func=lambda message: message.text == "Привет!")
def answer_hello(message):
    bot.send_message(message.chat.id, "и тебе привет, дорогой пользоватеь!")


@bot.message_handler(func=lambda message: message.text == "Помощь")
def help_command(message):
    bot.send_message(
        message.chat.id, "Я - учебный Бот. Пока я умею только здороваться!"
    )


@bot.message_handler(func=lambda message: message.text == "Пока")
def goodbuy_message(message):
    bot.send_message(message.chat.id, "и тебе досвидания мой дорогой друг!")


# add commands menu
@bot.message_handler(commands=["menu"])
def show_inline_menu(message):
    # Создаем объект клавиатуры
    markup = types.InlineKeyboardMarkup()

    # Создаем кнопки.
    # text — что видит юзер, callback_data — что "слышит" бот
    btn_yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    btn_no = types.InlineKeyboardButton(text="Нет", callback_data="no")

    # Добавляем кнопки в ряд
    markup.add(btn_yes, btn_no)

    bot.send_message(
        message.chat.id, "Тебе нравится изучать программирование", reply_markup=markup
    )


# 2. Создаем обработчик нажатий (callback)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # call.data — это то самое значение "yes" или "no"
    if call.data == "yes":
        bot.send_message(call.message.chat.id, "Круто! Продолжай в том же духе!")
    elif call.data == "no":
        bot.send_message(call.message.chat.id, "Ничего, скоро втянешься!")
    bot.answer_callback_query(call.id)


# Запуск бота
bot.infinity_polling()
