from telegram.ext import Updater, CommandHandler

from config import BOT_TOKEN, REQUEST_KWARGS, CHAT_ID, MONITORED_URL, SUBSTRING

STARTING_MESSAGE = 'monitoring up'


def starting_notification(bot, job):
    bot.send_message(chat_id=CHAT_ID, text=STARTING_MESSAGE)


def callback_monitor_1min(bot, job):
    bot.send_message(chat_id=CHAT_ID, text='One message every minute')


updater = Updater(BOT_TOKEN, request_kwargs=REQUEST_KWARGS)

j = updater.job_queue
j.run_once(starting_notification, 0)
j.run_repeating(callback_monitor_1min, interval=60, first=0)

updater.start_polling()
updater.idle()
