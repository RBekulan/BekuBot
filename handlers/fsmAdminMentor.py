from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from confing import bot
from keyboards import client_kb


class FSMAdmin(StatesGroup):
    id = State()
    name = State()
    direction = State()
    age = State()
    group = State()
    submit = State()


async def fsm_start(message: types.Message):
    if message.chat.type == 'private':
        await FSMAdmin.name.set()
        await message.answer("id?", reply_markup=client_kb.cancel_markup)
    else:
        await message.answer("Пиши  в личке ")


async def load_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = int(message.text)
    await FSMAdmin.next()
    await message.answer("Как зовут?", reply_markup=client_kb.cancel_markup)


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("какое напровления")


async def load_direction(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['direction'] = message.text
    await FSMAdmin.next()
    await message.answer("сколько лет", reply_markup=client_kb.cancel_markup)


async def load_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа")
    elif int(message.text) < 5 or int(message.text) > 50:
        await message.answer("Возростное ограничение!")
    else:
        async with state.proxy() as data:
            data['age'] = int(message.text)
        await FSMAdmin.next()
        await message.answer("группа какое?")


async def load_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text
    await FSMAdmin.next()
    await message.answer("Все ли провильно?")


async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == "да":
        # Запись в БД
        await state.finish()
        await message.answer("Ты зареган")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Ну и пошел ты!")
    else:
        await message.answer('НИПОНЯЛ!?')


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("пока")


def register_handlers_fsm_anketa(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, state="*", commands=['cancel'])
    dp.register_message_handler(cancel_fsm, Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['reg'])
    dp.register_message_handler(load_id, state=FSMAdmin.id)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_direction, state=FSMAdmin.direction)
    dp.register_message_handler(load_age, state=FSMAdmin.age)
    dp.register_message_handler(load_group, state=FSMAdmin.group)
    dp.register_message_handler(submit, state=FSMAdmin.submit)
