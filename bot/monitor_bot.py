import time
import logging
import os

from telegram.ext import Updater
import requests
from requests.exceptions import ConnectionError

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=os.path.join(BASE_DIR, "bot.log"), level=logging.ERROR,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


class MonitorBot:
    """ Bot monitors a url and sends notifications to Telegram channel. """
    STARTING_MESSAGE = 'monitoring up'
    MONITORING_INTERVAL = 1
    MIN_NOTIFICATION_PERIOD = 60

    def __init__(self, token, chat_id, monitored_url, substring, proxy=None):
        self.token = token
        self.chat_id = chat_id
        self.monitored_url = monitored_url
        self.substring = substring
        self.last_notified_time = 0.0
        self.WRONG_RESPONSE_MESSAGE = '{} is broken {} not found.'.format(monitored_url, substring)
        self.CONNECTION_ERROR_MESSAGE = '{} is not responding.'.format(monitored_url)
        self.proxy = proxy if proxy.get('proxy_url') else None

    def _callback_monitor(self, bot, job):
        """ Callback function. Makes requests and sends notifications. """
        warning_text = None
        try:
            response = requests.get(self.monitored_url)
        except ConnectionError:
            warning_text = self.CONNECTION_ERROR_MESSAGE
        else:
            if response.text != self.substring:
                warning_text = self.WRONG_RESPONSE_MESSAGE
        if warning_text:
            time_elapsed = time.time() - self.last_notified_time
            if time_elapsed > self.MIN_NOTIFICATION_PERIOD:
                self._send_warning(bot, warning_text)

    def _send_warning(self, bot, text, update=True):
        """ Send message to channel and update notification time. """
        try:
            bot.send_message(chat_id=self.chat_id, text=text)
        except Exception as e:
            logging.error(e)
        if update:
            self.last_notified_time = time.time()

    def start(self):
        """ Starts the bot. """
        self.updater = Updater(self.token, request_kwargs=self.proxy)
        # Notify the channel that the monitoring has started.
        self._send_warning(self.updater.bot, self.STARTING_MESSAGE, update=False)

        # Create repeating job queue
        j = self.updater.job_queue
        j.run_repeating(self._callback_monitor, interval=self.MONITORING_INTERVAL, first=0)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    from config import BOT_TOKEN, PROXY, CHAT_ID, MONITORED_URL, SUBSTRING

    mon_bot = MonitorBot(BOT_TOKEN, CHAT_ID, MONITORED_URL, SUBSTRING, proxy=PROXY)
    mon_bot.start()
