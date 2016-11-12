import dbcon


def start(bot, update):
    update.message.reply_text('Hello World!')


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


handler_func = {
    'start': start,
    'hello': hello
}
