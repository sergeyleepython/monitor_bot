fix.bot
=========

This role deploys bot to a specified host and runs it as a service.

Requirements
------------
* Python2
* Ansible
* RubyGems (for testing)


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
Install Ansible:
> $ $ sudo pip install ansible

Run ansible-playbook fix.bot.yml:
> $ ansible-playbook fix.bot.yml -b -K

Testing
--------------
For testing we use: Test Kitchen, kitchen-vagrant, kitchen-ansible and testinfra.

* Install RubyGems package manager.
> $ sudo apt-get install rubygems
* Install `test-kitchen`, `kitchen-vagrant` and `kitchen-ansible`:
> $ sudo gem install test-kitchen kitchen-vagrant kitchen-ansible

Run testing:
> $ cd roles/fix.bot

> $ kitchen test default-ubuntu

Author Information
------------------

Sergey Li