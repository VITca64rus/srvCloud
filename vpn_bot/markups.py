from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#Messages
ABOUT_BOT = 'Я — srvCloud VPN бот.\n\
Я подключу вас к VPN за пару простых шагов.\n\
\n\
Просто нажмите кнопку "Подключить VPN" и следуйте моим пошаговым инструкциям.'

CONNECT_VPN="🔌 Подключить VPN"
WRONG="'Упс🥺\nЧто-то пошло не так... Попробуйте позже'"

#Main menu
btnSub = KeyboardButton(CONNECT_VPN)
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True)
mainMenu.add(btnSub)

#Subscribe Inline Buttons
sub_inline_markup = InlineKeyboardMarkup(row_width=1)
btnSubMonth = InlineKeyboardMarkup(text="Mecяц - 100 рублей", callback_data="submonth")
sub_inline_markup.insert(btnSubMonth)
