from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
from confing import bot, dp

#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f"he i'm this Bekubot {message.from_user.first_name}")

#@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 1", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "номер GeekTech"
    answers = [
        '108',
        '106',
        '102',
        '103',
        '100',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="103",
        open_period=10,
        reply_markup=markup
    )


#@dp.message_handler(commands=['mem'])
async def mem_handler(message: types.Message):
    photo = open('mems/mem1.jfif', 'rb')
    await bot.send_photo(message.from_user.id, photo)

def regiter_handler_client(dp: Dispatcher):
    dp.register_message_handler(start_handler,commands=['start'])
    dp.register_message_handler(quiz_1,commands=['quiz'])
    dp.register_message_handler(mem_handler,commands=['mem'])
