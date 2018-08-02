# telegram bot token
BOT_TOKEN = 'XXXXXXXXXXXXXXX'

# proxy settings for Telegram
PROXY={
    'proxy_url': 'socks5://000.000.000.000:443',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'some_user',
        'password': 'some_password',
    }
}

# id of a telegram chat to send notifications
CHAT_ID = '1111111'

# url of monitored resource
MONITORED_URL = 'https://something'

# substring to search in a response
SUBSTRING = 'xxxxxx'

try:
    from config_local import *
except:
    pass
