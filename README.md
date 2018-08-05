Monitor Bot
=========
This bot monitors a website's state by sending a request to a specified url every 1 second and checking the presence of a specified substring in a response.

If the substring is absent, the bot sends warning to a specified Telegram chat id, but not more that once a minute.

## INSTALATION
There are two ways to install the bot. 

This document describes manual installation and launching.

You can also use Ansible to do it automatically. 
Use ansible playbook file `fix.bot.yml` as an example. 
See more details about the role in [`roles/fix.bot/README.md`](roles/fix.bot/README.md).

## REQUIREMENTS
Python 3.6

Python dependencies are listed in `requirements.txt`.

## DEPLOYMENT
* add a `config.py` file with your variables to the bot folder. 
For this, you can use an ansible template `roles/fix.bot/templates/config.py.j2`.

* copy the `bot` directory to a host server and enter it.

* install requirements.txt:
> pip3 install -r requirements.txt

## LAUNCHING AS A DEAMON

Add a file `bot.service` to `/etc/systemd/system/` of your host. 
For this, you can use an ansible template `roles/fix.bot/templates/bot.service.j2`.

Make the bot start automatically after OS is loaded:

> systemctl enable bot

Run the bot:
> systemctl start bot

## TESTING
> python3 tests.py
