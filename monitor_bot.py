from telegram.ext import Updater, CommandHandler

from config import BOT_TOKEN, REQUEST_KWARGS, CHAT_ID, MONITORED_URL, SUBSTRING


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater(BOT_TOKEN, request_kwargs=REQUEST_KWARGS)

updater.dispatcher.add_handler(CommandHandler('hello', hello))

updater.start_polling()
updater.idle()
