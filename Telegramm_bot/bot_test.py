import os
import webbrowser
from operator import call

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("Not token bot")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=["photo"])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    # site_button1 = types.InlineKeyboardButton(
    #     text="Перейти на сайт YOUTUBE...", url="https://youtube.com"
    # )
    # site_button2 = types.InlineKeyboardButton(
    #     text="Перейсти на сайт GOOGLE...", url="https://google.com"
    # )
    # site_button3 = types.InlineKeyboardButton(
    #     text="Удалить фото", callback_data="delete"
    # )
    # site_button4 = types.InlineKeyboardButton(
    #     text="Изменить фото", callback_data="edit"
    # )
    # markup.add(site_button1, site_button2, site_button3, site_button4)

    markup.add(types.InlineKeyboardButton(text="ютуб", url="https://youtube.com"))
    markup.add(types.InlineKeyboardButton(text="гугл", url="https://google.com"))
    markup.add(types.InlineKeyboardButton(text="удалить", callback_data="delete"))
    markup.add(types.InlineKeyboardButton(text="редактирвоать", callback_data="edit"))

    bot.reply_to(message, "Какое красивое фото!", reply_markup=markup)



@bot.message_handler(commands=["site", "website"])
def site(message):
    webbrowser.open("https://youtube.com")


@bot.message_handler(commands=["start", "main", "hello"])
def handler_start(message) -> None:
    bot.send_message(
        message.chat.id,
        f"Hello, {message.from_user.first_name},{message.from_user.last_name}",
    )

    # raw_data = str(message)
    # bot.send_message(
    #     message.chat.id,
    #     "<b>Здорова Братан</b>, <em><u>как дела? Как сам....</u></em>",
    #     parse_mode="html",
    # )
    # bot.send_message(message.chat.id, raw_data[:2000])


@bot.message_handler(commands=["help"])
def handler_help(message):
    bot.send_message(message.chat.id, "Привет, с чем тебе мопочь ?")


@bot.message_handler()
def info(message) -> None:
    if message.text.lower() == "hello":
        bot.send_message(
            message.chat.id,
            f"Hello, {message.from_user.first_name},{message.from_user.last_name}",
        )
    elif message.text.lower() == "id":
        bot.reply_to(message, f"ID: {message.from_user.id}")


bot.polling(none_stop=True)
