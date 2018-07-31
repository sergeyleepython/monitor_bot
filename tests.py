import unittest
from unittest.mock import patch, Mock

from monitor_bot import MonitorBot


class TestMonitorBot(unittest.TestCase):
    def setUp(self):
        self.BOT_TOKEN = 'test'
        self.REQUEST_KWARGS = {
            'proxy_url': 'socks5://1.1.1.1:443',
            'urllib3_proxy_kwargs': {
                'username': 'test',
                'password': 'test',
            }
        }
        self.CHAT_ID = 'test'
        self.MONITORED_URL = 'http://test'
        self.SUBSTRING = 'test'
        self.mon_bot = MonitorBot(self.BOT_TOKEN, self.REQUEST_KWARGS, self.CHAT_ID, self.MONITORED_URL, self.SUBSTRING)

    @patch('monitor_bot.MonitorBot._send_warning')
    @patch('monitor_bot.requests.get')
    def test_callback_monitor(self, get, send_warning):
        bot = Mock()
        job = Mock()
        self.mon_bot._callback_monitor(bot, job)
        get.assert_called_with(self.MONITORED_URL)
        send_warning.assert_called_with(bot)

    def test_send_warning(self):
        bot = Mock()
        old_last_notified_time = self.mon_bot.last_notified_time
        self.mon_bot._send_warning(bot)
        self.assertNotEqual(old_last_notified_time, self.mon_bot.last_notified_time)


if __name__ == '__main__':
    unittest.main()
