from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import dp, bot
from aiogram.dispatcher.filters import Text
from data_base import sql_db
import keyboard_main

class Bron(StatesGroup):
    sost1 = State()

async def bron1(message: types.Message):
    await message.reply("Введите желаемое день и время посещения нашего заведения, зал, в которомы вы"
                        "желаете расположиться (в одном сообщении). "
                        "Для отмены бронирования нажмите кнопку 'Отмена'",
                        reply_markup=keyboard_main.kb_zakaz)
    await Bron.sost1.set()


async def bron2(message : types.Message, state = FSMContext):
    bron = await sql_db.bron(message)
    await state.finish()
    master = await sql_db.master()
    await bot.send_message(master[0], f"номер {bron[0][0][0]} @{bron[3][0][0]} ,бронь на {bron[1][0][0]} ")
    await message.reply("В ближайшее время вам поступит ответ по вашему бронированию",
                        reply_markup=keyboard_main.ikb_uslugi)


async def cancel(message : types.Message, state = FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply("OK")

@dp.message_handler(lambda message: message.text.lower() in ["кто на смене?", '/master'])
async def masters(message: types.Message):
    master = await sql_db.master()
    await bot.send_photo(message.from_user.id, f"{master[1]}")
    await bot.send_message(message.from_user.id, f"На смене {master[2]}", reply_markup=keyboard_main.ikb_main)

def registr_client(dp: Dispatcher):
    dp.register_message_handler(bron1, lambda message: message.text in ["Забронировать стол", "/reservation"], state=None)
    dp.register_message_handler(cancel, state="*", commands=['отмена', 'cancel'])
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")
    dp.register_message_handler(bron2, state=Bron.sost1)