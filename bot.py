import telebot
bot_config=open("config.txt")
token=bot_config.readline().strip()
def send_tg(information):
    bot = telebot.TeleBot(token)
    for i in range(10):
        bot.send_message("@parser_channel", information)
    bot.polling()
