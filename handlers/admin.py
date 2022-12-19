import random

from confing import bot, dp
from aiogram import types, Dispatcher


async def game(message: types.Message):
    games = ['🏀', '⚽', '🎰', '🎳', '🎯', '🎲']
    emoji = random.choice(games)
    await bot.send_dice(message.from_user.id, emoji=emoji)


def register_handler_admin(dp: Dispatcher):
    dp.register_message_handler(game, commands=['game'])
