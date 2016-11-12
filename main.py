from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, ChosenInlineResultHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import config
import handler
import logger

def main():

    tokenKey = config.ConfigSectionMap('CONFIG')['token']
    updater = Updater(tokenKey)  # get tokenKey from config.ini file
    # loop through each handler in handler.py


    for command, fhandler in handler.handler_func.items():
        updater.dispatcher.add_handler(CommandHandler(command, fhandler))

    updater.dispatcher.add_handler(CallbackQueryHandler(handler.button))
    # updater.dispatcher.add_handler(ChosenInlineResultHandler(handler.process_result))
    updater.dispatcher.add_error_handler(handler.error)
    # start the bot polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
