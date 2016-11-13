import telebot
from telebot import types
import logger
import config
import handler
def main():
    tokenKey = config.ConfigSectionMap('CONFIG')['token2']
    handler.Handler(tokenKey)

if __name__ == '__main__':
    main()
