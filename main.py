import telebot
from telebot import types
# import handler
import logger
import config
def main():
    tokenKey = config.ConfigSectionMap('CONFIG')['token2']
    # loop throuagh each handler in handler.py


    bot = telebot.TeleBot(tokenKey)

    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Hello! Welcome to PingBot!")
        markup = types.ReplyKeyboardMarkup(row_width=2)
        add = types.KeyboardButton('Add Website')
        edit = types.KeyboardButton('Edit Website')
        delete = types.KeyboardButton('Delete Website')
        credit = types.KeyboardButton('Credits')
        markup.add(add, edit, delete, credit)
        bot.reply_to(message,'Select A Function Below', reply_markup=markup)

    @bot.message_handler(func=lambda message: True)
    def echo_all(message):
        # bot.reply_to(message, message.text)
        if message.text == 'Add Website':
            addweb(message)
        elif message.text == 'Edit Website':
            editweb(message)
        elif message.text == 'Delete Website':
            deleteweb(message)
        elif message.text == 'Credits':
            credit(message)

    def addweb(message):
        chat_id = message.chat.id
        bot.send_message(chat_id,'Add!')

    def editweb(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'editweb!')

    def deleteweb(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'deleteweb!')

    def credit(message):
        chat_id = message.chat.id
        bot.send_message(chat_id, 'credit!')

    bot.polling()

if __name__ == '__main__':
    main()
