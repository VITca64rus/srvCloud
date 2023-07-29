from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import json

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

#Subscribe steps
SUBSCRIBE_FIRST_STEP="🔌 ПОДКЛЮЧЕНИЕ К VPN\n\
\n\
ШАГ 1 ИЗ 5\n\
\n\
Выберите регион вашего VPN подключения"


COUNTY={
    'Нидерланды': '🇳🇱 Нидерланды'
}

def create_keyboard_products(products):
    '''Create keyboard'''
    sub_inline_markup = InlineKeyboardMarkup(row_width=products.get('total_records'))
    for product in products.get('data'):
        btn = InlineKeyboardMarkup(text=COUNTY.get(product.get('name')),
                                   callback_data=product.get('id'))
        sub_inline_markup.insert(btn)
    return sub_inline_markup
