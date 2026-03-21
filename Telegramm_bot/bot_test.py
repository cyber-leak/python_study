import os
import webbrowser

import telebot
from dotenv import load_dotenv
from telebot import types

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("Not token bot")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    site_button1 = types.KeyboardButton(text="Перейти на сайт YOUTUBE...")
    site_button2 = types.KeyboardButton(text="Перейсти на сайт GOOGLE...")
    site_button3 = types.KeyboardButton(text="Удалить фото")
    site_button4 = types.KeyboardButton(text="Изменить фото")

    markup.add(site_button1, site_button2, site_button3, site_button4)
    with open("photo.jpeg", "rb") as file:
        # file = open("./photo.jpeg", "rb")
        bot.send_document(message.chat.id, file, reply_markup=markup)
        # bot.send_photo(message.chat.id, file, reply_markup=markup)
        # bot.send_audio(message.chat.id, file, reply_markup=markup)
        # bot.send_video(message.chat.id, file, reply_markup=markup)
        
        

    bot.send_message(message.chat.id, "HI", reply_markup=markup)

    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == "Перейти на сайт YOUTUBE...":
        bot.send_message(message.chat.id, "Website is open YOUTUBE.")

    elif message.text == "Перейсти на сайт GOOGLE...":
        bot.send_message(message.chat.id, "Website is open GOOGLE.")

    elif message.text == "Удалить фото":
        bot.send_message(message.chat.id, "Delete photo")

    elif message.text == "Изменить фото":
        bot.send_message(message.chat.id, "Edit photo")

    else:
        bot.send_message(message.chat.id, "что то пошло не так....")


# @bot.message_handler(content_types=["photo"])
# def get_photo(message):
#     markup = types.InlineKeyboardMarkup(row_width=2)
#     site_button1 = types.InlineKeyboardButton(
#         text="Перейти на сайт YOUTUBE...", url="https://youtube.com"
#     )
#     site_button2 = types.InlineKeyboardButton(
#         text="Перейсти на сайт GOOGLE...", url="https://google.com"
#     )
#     site_button3 = types.InlineKeyboardButton(
#         text="Удалить фото", callback_data="delete"
#     )
#     site_button4 = types.InlineKeyboardButton(
#         text="Изменить фото", callback_data="edit"
#     )
#     # markup.row(site_button1)
#     # markup.row(site_button2, site_button3)
#     markup.add(site_button1, site_button2, site_button3, site_button4)

#     # markup.add(types.InlineKeyboardButton(text="ютуб", url="https://youtube.com"))
#     # markup.add(types.InlineKeyboardButton(text="гугл", url="https://google.com"))
#     # markup.add(types.InlineKeyboardButton(text="удалить", callback_data="delete"))
#     # markup.add(types.InlineKeyboardButton(text="редактирвоать", callback_data="edit"))

#     bot.reply_to(message, "Какое красивое фото!", reply_markup=markup)


# @bot.callback_query_handler(func=lambda callback: True)
# def callback_message(callback):
#     if callback.data == "delete":
#         try:
#             ids_to_delete = [
#                 callback.message.message_id,
#                 callback.message.reply_to_message.message_id,
#             ]
#             bot.delete_messages(callback.message.chat.id, ids_to_delete)
#         except Exception as e:
#             print(e)
#             bot.delete_message(callback.message.chat.id, callback.message.message_id)

#     elif callback.data == "edit":
#         bot.edit_message_text(
#             "Edit text", callback.message.chat.id, callback.message.message_id
#         )


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
