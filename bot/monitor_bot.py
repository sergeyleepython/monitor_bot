import time

from telegram.ext import Updater
import requests
from requests.exceptions import ConnectionError

from config import BOT_TOKEN, PROXY, CHAT_ID, MONITORED_URL, SUBSTRING


class MonitorBot:
    """ Bot monitors a url and sends notifications to Telegram channel. """
    STARTING_MESSAGE = 'monitoring up'
    MONITORING_INTERVAL = 1
    MIN_NOTIFICATION_PERIOD = 60

    def __init__(self, token, proxy, chat_id, monitored_url, substring):
        self.token = token
        self.proxy = proxy
        self.chat_id = chat_id
        self.monitored_url = monitored_url
        self.substring = substring
        self.last_notified_time = 0.0
        self.WRONG_RESPONSE_MESSAGE = '{} is broken {} not found.'.format(monitored_url, substring)
        self.CONNECTION_ERROR_MESSAGE = '{} is not responding.'.format(monitored_url)

    def _callback_monitor(self, bot, job):
        """ Callback function. Makes requests and sends notifications. """
        warning_text = None
        try:
            response = requests.get(self.monitored_url)
        except ConnectionError:
            warning_text=self.CONNECTION_ERROR_MESSAGE
        else:
            if response.text != self.substring:
                warning_text=self.WRONG_RESPONSE_MESSAGE
        if warning_text:
            time_elapsed = time.time() - self.last_notified_time
            if time_elapsed > self.MIN_NOTIFICATION_PERIOD:
                self._send_warning(bot, warning_text)

    def _send_warning(self, bot, text):
        """ Send message to channel and update notification time. """
        bot.send_message(chat_id=CHAT_ID, text=text)
        self.last_notified_time = time.time()

    def start(self):
        """ Starts the bot. """
        self.updater = Updater(self.token, request_kwargs=self.proxy)
        # Notify the channel that the monitoring has started.
        self.updater.bot.send_message(chat_id=self.chat_id, text=self.STARTING_MESSAGE)

        # Create repeating job queue
        j = self.updater.job_queue
        j.run_repeating(self._callback_monitor, interval=self.MONITORING_INTERVAL, first=0)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    mon_bot = MonitorBot(BOT_TOKEN, PROXY, CHAT_ID, MONITORED_URL, SUBSTRING)
    mon_bot.start()
