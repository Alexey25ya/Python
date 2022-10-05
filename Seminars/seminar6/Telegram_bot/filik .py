from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from config import TOKEN
from fuction import * 


bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
info_handler = CommandHandler('info', info)
delete_handler =CommandHandler('delete', delete_word)
message_handler = MessageHandler(Filters.text, give_word)
unknown_handler = MessageHandler(Filters.command, unknown)  # /game


dispatcher.add_handler(start_handler)
dispatcher.add_handler(info_handler)
dispatcher.add_handler(delete_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)


print('server started')
updater.start_polling()
updater.idle()




