from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")

b_time = KeyboardButton("Режим работы")
b_adress = KeyboardButton("Адрес")
b_contacts = KeyboardButton("Контакты")
b_first = KeyboardButton("В начало")
b_usligi = KeyboardButton("Услуги нашего заведения")
b_about = KeyboardButton("О нашем кафе")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow.row(b_usligi).row(b_about)

b_masters = KeyboardButton("Наши мастера")
b_interier = KeyboardButton("Интерьер")
b_tells = KeyboardButton("Отзывы")
ib_about = InlineKeyboardButton(text="Назад", callback_data="О нашем кафе")
ib_next_photo = InlineKeyboardButton(text="Следующее фото", callback_data="next_photo")
ib_next_tell = InlineKeyboardButton(text="Cлучайный отзыв", callback_data="next_tell")
kb_ourbar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ourbar.row(b_interier).row(b_time, b_adress, b_contacts).row(b_tells)
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)
ikb_about = InlineKeyboardMarkup(row_width=1).row(ib_about, ib_next_photo)
ikb_tells = InlineKeyboardMarkup(row_width=1).row(ib_main, ib_next_tell)

b_hooka = KeyboardButton("Кальянные радости")
b_menu = KeyboardButton("Меню")
b_stol = KeyboardButton("Забронировать стол")
kb_uslugi = ReplyKeyboardMarkup(resize_keyboard=True)
kb_uslugi.row(b_menu).row(b_hooka,).row(b_stol)

b_zakus = KeyboardButton("Закуски")
b_salat = KeyboardButton("Салаты")
b_brekfast = KeyboardButton("Завтраки")
b_hot = KeyboardButton("Горячие блюда")
b_burger = KeyboardButton("Бургер-сет")
b_pizza = KeyboardButton("Пицца")
b_bar = KeyboardButton("Напитки")
kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
kb_menu.row(b_zakus, b_salat, b_bar).row(b_brekfast, b_hot).row(b_burger, b_pizza)


ib_uslugi = InlineKeyboardButton(text="Назад", callback_data="Услуги нашего заведения")
b_tea = KeyboardButton("Чаи")
b_cold = KeyboardButton("Прохладительные напитки")

kb_bar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_bar.row(b_tea).row(b_cold).row(b_stol)
ikb_uslugi = InlineKeyboardMarkup(row_width=1).row(ib_uslugi, ib_main)

b_tell_about = KeyboardButton("Оставить отзыв")
b_read_about = KeyboardButton("Ознакомиться с отзывами")
kb_tells = ReplyKeyboardMarkup(resize_keyboard=True)
kb_tells.row(b_tell_about).row(b_read_about)


b_nasmene = KeyboardButton("Я на смене")
b_bron_accapt = KeyboardButton("Подтвердить бронь")
b_tell_accapt = KeyboardButton("Разрешить отзыв")
b_bron_no = KeyboardButton("Послать нахуй")
b_spam = KeyboardButton("Запилить рассылку")
kb_mainwindow_admin = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow_admin.row(b_nasmene).row(b_bron_accapt, b_bron_no).row(b_tell_accapt).row(b_spam)

b_cancel = KeyboardButton("Отмена")
ib_cancel = InlineKeyboardButton(text="Отмена", callback_data="cancel")
ikb_cancel = InlineKeyboardMarkup(row_width=1).row(ib_cancel)

kb_zakaz = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zakaz.row(b_cancel).row(b_usligi)

b_who_at_work = KeyboardButton("Кто на смене?")
kb_who_at_work = ReplyKeyboardMarkup(resize_keyboard=True).row(b_who_at_work).row(b_first)

