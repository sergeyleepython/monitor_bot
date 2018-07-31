from telegram.ext import Updater
import requests

from config import BOT_TOKEN, REQUEST_KWARGS, CHAT_ID, MONITORED_URL, SUBSTRING

STARTING_MESSAGE = 'monitoring up'


def callback_start(bot, job):
    bot.send_message(chat_id=CHAT_ID, text=STARTING_MESSAGE)


def callback_monitor_1sec(bot, job):
    response = requests.get(MONITORED_URL)
    if response.text != SUBSTRING:
        print('{} is broken {} not found.'.format(MONITORED_URL, SUBSTRING))
    else:
        print('OK!')


def callback_notify_1min(bot, job):
    bot.send_message(chat_id=CHAT_ID, text='One message every minute')


updater = Updater(BOT_TOKEN, request_kwargs=REQUEST_KWARGS)

j1 = updater.job_queue
j2 = updater.job_queue
j3 = updater.job_queue
j1.run_once(callback_start, 0)
j2.run_repeating(callback_monitor_1sec, interval=1, first=0)
j3.run_repeating(callback_notify_1min, interval=60, first=0)

updater.start_polling()
updater.idle()

# todo: replace with class
# todo: add last_notified attribute (datetime)