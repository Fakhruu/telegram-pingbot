def main():
    tokenKey = config.ConfigSectionMap('CONFIG')['token']
    # loop throuagh each handler in handler.py


    bot = telebot.TeleBot(tokenKey)

    @bot.message_handler(commands=['start', 'help'])
    def send_welcome(message):
        bot.reply_to(message, "Howdy, how are you doing?")

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        bot.reply_to(message, message.text)

    bot.polling()

if __name__ == '__main__':
    main()
