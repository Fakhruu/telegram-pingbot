from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import dbcon

datafakap = ()

def start(bot, update):
    update.message.reply_text('Hello World!')

<<<<<<< HEAD
def menu(bot, update):
    global datafakap
    datafakap=(bot, update)
    keyboard =  [[InlineKeyboardButton("Add Website", callback_data='/add'),
                InlineKeyboardButton("Edit Website", callback_data='/edit')],
                [InlineKeyboardButton("Delete Website", callback_data='/delete'),
                InlineKeyboardButton("Credits", callback_data='/credit')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)
>>>>>>> 4bfdb9c5e0077b64261a8432e6bf05b0363883b5

def add(bot, update):
    update.message.reply_text('Add Website Function Goes Here')

def edit(bot, update):
    update.message.reply_text('Edit Website Function Goes Here')

def delete(bot, update):
    update.message.reply_text('Delete Website Function Goes Here')

def credit(bot, update):
    update.message.reply_text('Credit')

def error(bot, update, error):
    logging.warning('Update "%s" caused error "%s"' % (update, error))

handler_func = {
    'start': start,
    'menu': menu,
    'add' : add,
    'edit': edit,
    'delete': delete,
    'credit': credit
}

def button(bot, update):
    global datafakap
    query = update.callback_query
    handler_func[query.data[1:]](*datafakap)

    bot.editMessageText(text="Selected option: %s" % query.data,
                        chat_id=query.message.chat_id,
                        message_id=query.message.message_id)
