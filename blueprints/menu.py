import random

from vkbottle.bot import Message, Blueprint

from json_data import cards

bp = Blueprint("main_menu")


@bp.on.private_message(text=["Старт", 'старт'])
async def games_menu(message: Message):
    cards_attachments = random.sample(list(cards), 5)
    await message.answer('Начинаем игру!', attachment=cards_attachments)
