from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram import Bot, Dispatcher, types
from confing import bot, dp



#@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT 2", callback_data="button_call_2")
    markup.add(button_call_1)

    question = "как называется напровление IT которое занимается логикой сайтов"
    answers = [
        "back end",
        "front end",
        "UX UI",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Стыдно не знать",
        open_period=5,
        reply_markup=markup
    )

#@dp.callback_query_handler(text="button_call_1")
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT 3", callback_data="button_call_3")
    markup.add(button_call_2)

    question = "сколько месец в ондом году"
    answers = [
        "24",
        "12",
        "11"
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="в ондом году 12 месецов",
        open_period=5,
        reply_markup=markup
    )

def register_handler_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,text="button_call_1",)
    dp.register_callback_query_handler(quiz_3,text="button_call_2",)