import telebot

bot_config = open("config.txt")
token = bot_config.readline().strip()


def send_tg(information):
    bot = telebot.TeleBot(token)
    bot.send_message("@parser_channel", information)
# send_tg("Life is a show")
