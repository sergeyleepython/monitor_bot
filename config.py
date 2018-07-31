# telegram bot token
BOT_TOKEN = 'XXXXX'

# id of a telegram chat to send notifications
CHAT_ID = 1111111

# url of monitored resource
MONITORED_URL = 'https://something'

# substring to search in a response
SUBSTRING = 'xxxxxx'

try:
    from config_local import *
except:
    pass