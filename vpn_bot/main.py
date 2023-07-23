import logging
import os

import markups as nav
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)
#Initialize bot
bot = Bot(token=os.environ.get('TGBOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start' ])
async def start (message: types.Message):
    '''Command start'''
    message_start = f'🖖 Привет {message.from_user.first_name}!\n\n{nav.ABOUT_BOT}'
    await bot.send_message(message.from_user.id, message_start, reply_markup = nav.mainMenu)


@dp.message_handler ()
async def bot_message(message: types.Message):
    '''Обработка входящих сообщений'''
    if message.chat.type == 'private':
        if message.text == nav.CONNECT_VPN:
            await bot.send_message(message.from_user.id,
                                   "После оплаты подписки я пришлю Вам ovpn фаил для доступа через приложение openVPN",
                                   reply_markup = nav.sub_inline_markup)


@dp.callback_query_handler(text="submonth")
async def submonth(call: types.CallbackQuery):
    '''Запрос в Юкассу'''
    await bot.send_invoice(chat_id=call.from_user.id,
                           title="VPN Нидерданды",
                           description="Доступ на месяц",
                           payload="VPN_niderlands_mounth",
                           provider_token=os.environ.get('YKASSA_TOKEN'),
                           currency="RUB",
                           start_parameter="test",
                           prices=[
                                    {"label": "Руб",
                                    "amount": 10000
                                    }
                                  ]
                           )


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.pre_checkout_query):
    '''Проверка наличия товара'''
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.message):
    '''Проверка корректности оплаты'''
    if message.successful_payment.invoice_payload == 'VPN_niderlands_mounth':
        await message.reply_document(open('/home/vpodlevski/Desktop/test0.ovpn', 'rb'))


executor.start_polling(dp, skip_updates = True)