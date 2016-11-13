import telebot
from telebot import types


class Handler:

    def __init__(self, tokenKey):

        """
        # register the bot token with pytelegram
        """
        self.bot = telebot.TeleBot(tokenKey)

        """
        # Register modules for the use of telegram bot
        """
        @self.bot.message_handler(commands=['start'])
        def send_welcome(message):
            self.bot.reply_to(message, "Hello! Welcome to PingBot!")
            self.show_menu(message)

        @self.bot.message_handler(commands=['menu'])
        def open_menu(message):
            self.show_menu(message)

        @self.bot.message_handler(func=lambda message: message.text == 'derp')
        def echo_all(message):
            self.bot.send_message(message.chat.id, 'derp!')

        @self.bot.message_handler(func=lambda message: True)
        def echo_all(message):
            if message.text == 'Add Website':
                self.addweb(message)
            elif message.text == 'Edit Website':
                self.editweb(message)
            elif message.text == 'Delete Website':
                self.deleteweb(message)
            elif message.text == 'Credits':
                self.credit(message)
            else:
                self.bot.send_message(message.chat.id, "I don't understand " + message.text+ "please click /menu")

        """
        # poll the bot for user requests
        """
        self.bot.polling()

    def addweb(self, message):
        chat_id = message.chat.id
        self.bot.send_message(chat_id,'Please insert your website domain below: ')
        self.bot.register_next_step_handler(message, self.weburl)

    def weburl(self, message):
        url = message.text
        self.bot.send_message(message.chat.id, "Your URL: " + url)

    def editweb(self, message):
        chat_id = message.chat.id
        self.bot.send_message(chat_id, 'editweb!')

    def deleteweb(self, message):
        chat_id = message.chat.id
        self.bot.send_message(chat_id, 'deleteweb!')

    def credit(self, message):
        chat_id = message.chat.id
        self.bot.send_message(chat_id, 'credit!')

    def show_menu(self, message):
        markup = types.ReplyKeyboardMarkup(row_width=2, one_time_keyboard=True)
        add = types.KeyboardButton('Add Website')
        edit = types.KeyboardButton('Edit Website')
        delete = types.KeyboardButton('Delete Website')
        credit = types.KeyboardButton('Credits')
        markup.add(add, edit, delete, credit)
        self.bot.reply_to(message, 'Select A Function Below', reply_markup=markup)
