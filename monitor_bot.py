import time

from telegram.ext import Updater
import requests

from config import BOT_TOKEN, REQUEST_KWARGS, CHAT_ID, MONITORED_URL, SUBSTRING


class MonitorBot:
    """ Bot monitors a url and sends notifications to Telegram channel. """
    STARTING_MESSAGE = 'monitoring up'
    MONITORING_INTERVAL = 1
    MIN_NOTIFICATION_PERIOD = 60

    def __init__(self, token, request_kwargs, chat_id, monitored_url, substring):
        self.token = token
        self.request_kwargs = request_kwargs
        self.chat_id = chat_id
        self.monitored_url = monitored_url
        self.substring = substring
        self.last_notified_time = 0.0
        self.WARNING_MESSAGE = '{} is broken {} not found.'.format(monitored_url, substring)

    def _callback_monitor(self, bot, job):
        """ Callback function. Makes requests and sends notifications. """
        response = requests.get(self.monitored_url)
        if response.text != self.substring:
            time_elapsed = time.time() - self.last_notified_time
            if time_elapsed > self.MIN_NOTIFICATION_PERIOD:
                self._send_warning(bot)

    def _send_warning(self, bot):
        """ Send message to channel and update notification time. """
        bot.send_message(chat_id=CHAT_ID, text=self.WARNING_MESSAGE)
        self.last_notified_time = time.time()

    def start(self):
        """ Starts the bot. """
        self.updater = Updater(self.token, request_kwargs=self.request_kwargs)
        # Notify the channel that the monitoring has started.
        self.updater.bot.send_message(chat_id=self.chat_id, text=self.STARTING_MESSAGE)

        # Create repeating job queue
        j = self.updater.job_queue
        j.run_repeating(self._callback_monitor, interval=self.MONITORING_INTERVAL, first=0)

        self.updater.start_polling()
        self.updater.idle()


if __name__ == '__main__':
    mon_bot = MonitorBot(BOT_TOKEN, REQUEST_KWARGS, CHAT_ID, MONITORED_URL, SUBSTRING)
    mon_bot.start()
