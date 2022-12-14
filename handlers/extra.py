from confing import bot, dp
from aiogram import Bot, Dispatcher, types


#@dp.message_handler()
async def echo(message: types.Message):
    if message.text.startswith('!pin'):
        await bot.pin_chat_message(message.chat.id, message.message_id)


def register_handler_extra(dp: Dispatcher):
    dp.register_message_handler(echo)
