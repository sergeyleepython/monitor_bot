def test_bot_is_running_and_enabled(host):
    bot = host.service("bot")
    assert bot.is_running
    assert bot.is_enabled
