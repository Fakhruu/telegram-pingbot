from telegram.ext import Updater, CommandHandler
import config
import handler


def main():

    tokenKey = config.ConfigSectionMap('CONFIG')['token']
    updater = Updater(tokenKey)  # get tokenKey from config.ini file

    # loop through each handler in handler.py
    for command, fhandler in handler.handler_func.items():
        updater.dispatcher.add_handler(CommandHandler(command, fhandler))

    # start the bot polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
