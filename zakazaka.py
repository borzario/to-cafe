from aiogram import types

import keyboard_main
from create_bot import dp, bot


@dp.callback_query_handler(text="z_pizza")
async def z_pizza(message: types.Message):
    await bot.send_message(message.from_user.id, "Выберите пиццу", reply_markup=keyboard_main.ikb_types_of_pizza)
