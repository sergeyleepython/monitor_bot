fix.bot
=========

This role deploys bot to a specified host and runs it as a service.

Requirements
------------
Python2, SSH


Role Variables
--------------

Specify your variables in `defaults/main.yml`. Template is provided.

Description:

* `bot_token` - Telegram bot token.

* `chat_id` - Telegram chat id or channel name, where the notification will be sent.

* `monitored_url` - URL of the monitored resource.

* `substring` - string value which should be in response.

Specify proxy settings if Telegram is blocked in your country:

* `proxy_url`

* `proxy_username`

* `proxy_password`


Example Playbook
----------------

    - hosts: fix1
      gather_facts: false
      roles:
         - role: fix.bot

Launching example
----------------
> ansible-playbook fix.bot.yml -b -K

Author Information
------------------

Sergey Li