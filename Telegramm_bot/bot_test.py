import os

import telebot
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    raise ValueError("Not token bot")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "main", "hello"])
def handler_start(message):
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


bot.polling(none_stop=True)
