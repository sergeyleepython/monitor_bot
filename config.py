# telegram bot token
BOT_TOKEN = 'XXXXX'

REQUEST_KWARGS={
    'proxy_url': 'URL_OF_THE_PROXY_SERVER',
    # Optional, if you need authentication:
    'urllib3_proxy_kwargs': {
        'username': 'PROXY_USER',
        'password': 'PROXY_PASS',
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
