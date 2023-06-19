from aiogram import types


import keyboard_main
from create_bot import dp, bot
from data_base import sql_db



@dp.callback_query_handler(text="z_pizza")
async def z_pizza(cb: types.CallbackQuery):
    await bot.edit_message_text(message_id=cb.message.message_id, chat_id=cb.message.chat.id, text="Выберите пиццу",
                                reply_markup=keyboard_main.ikb_types_of_pizza)


@dp.callback_query_handler(lambda c: c.data[:5] == "zakp ")
async def z_pizza_zak(cb: types.CallbackQuery):
    await sql_db.add_zak(cb.from_user.id, cb.data[5:])
    await bot.answer_callback_query(cb.id, text=f"Товар добавлен в корзину", show_alert=True)


@dp.callback_query_handler(lambda c: "корзина" in c.data)
@dp.message_handler(lambda message: "корзина" in message.text.lower())
async def look_korzina(message: types.Message):
    korz: list = await sql_db.get_tov_from_korzina(message.from_user.id)
    gods_list = ''
    gods_cost = 0
    for i in korz:
        gods_list += f"{i[0]} - {i[2]}, {i[3]} рублей\n"
        gods_cost += i[3]
    await bot.send_message(message.from_user.id, f"Ваш заказ:\n{gods_list}Стоимость заказа: {gods_cost} рублей",
                           reply_markup=keyboard_main.ikb_clear_pay)
