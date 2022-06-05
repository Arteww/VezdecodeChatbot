from vkbottle import Bot

from blueprints import bps

from config import api, db


def setup_blueprints(bot_: Bot):
    for bp in bps:
        bp.load(bot_)


def setup_middlewares(bot_: Bot):
    pass


def init_bot():
    bot_ = Bot(api=api)
    setup_middlewares(bot_)
    setup_blueprints(bot_)
    return bot_


async def init_db():
    pass


bot = init_bot()
bot.loop_wrapper.on_startup.append(init_db())
