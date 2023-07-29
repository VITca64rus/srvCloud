import logging
import os

import markups as nav
import srv_cloud_helper
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

logging.basicConfig(level=logging.INFO)
#Initialize bot
bot = Bot(token=os.environ.get('TGBOT_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start' ])
async def start (message: types.Message):
    '''Command start'''
    if message.chat.type == 'private':
        if await srv_cloud_helper.add_user(message.from_user.id,
                                           message.from_user.first_name,
                                           message.from_user.last_name,
                                           message.from_user.username) is False:
            await bot.send_message(message.from_user.id, nav.WRONG, reply_markup = nav.mainMenu)
        message_start = f'🖖 Привет {message.from_user.first_name}!\n\n{nav.ABOUT_BOT}'
        await bot.send_message(message.from_user.id, message_start, reply_markup = nav.mainMenu)


@dp.message_handler ()
async def bot_message(message: types.Message):
    '''Обработка входящих сообщений'''
    if message.chat.type == 'private':
        if message.text == nav.CONNECT_VPN:
            params = {
                'mode': 'get_vpns'
            }
            products_vpn = await srv_cloud_helper.get_products_vpn(params)
            products_keyboard = nav.create_keyboard_products(products_vpn)
            await bot.send_message(message.from_user.id,
                                   nav.SUBSCRIBE_FIRST_STEP,
                                   reply_markup = products_keyboard)


@dp.callback_query_handler()
async def subscribe(call: types.CallbackQuery):
    '''Запрос в Юкассу'''
    id_product = call.data
    params = {
        'filter_id': id_product,
        'mode': 'get_vpns'
    }
    products_vpn = await srv_cloud_helper.get_products_vpn(params)
    if products_vpn.get('total_records') != 1:
        await bot.send_message(call.from_user.id, nav.WRONG, reply_markup = nav.mainMenu)
        return 1
    product = products_vpn.get('data')[0]
    await bot.send_invoice(chat_id=call.from_user.id,
                           title=f"{nav.COUNTY.get(product.get('name'))} VPN",
                           description=product.get('description'),
                           payload=product.get('payload'),
                           provider_token=os.environ.get('YKASSA_TOKEN'),
                           currency=product.get('currency'),
                           start_parameter="test",
                           prices=[
                                    {"label": product.get('price_label'),
                                    "amount": product.get('price_amount') * 100
                                    }
                                  ]
                           )


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.pre_checkout_query):
    '''Проверка наличия товара'''
    params = {
        'filter_payload': pre_checkout_query.invoice_payload,
        'filter_active': 'true',
        'mode': 'get_subscriptions'
    }
    products_vpn = await srv_cloud_helper.get_products_vpn(params)
    if products_vpn.get('total_records') < 20:
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)
    else:
        await bot.answer_pre_checkout_query(
            pre_checkout_query.id,
            ok=False,
            error_message='К сожалению подписки закончились. Выберете другую страну'
        )


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message: types.message):
    '''Проверка корректности оплаты'''
    params = {
        'filter_payload': message.successful_payment.invoice_payload,
        'mode': 'get_vpns'
    }
    products_vpn = await srv_cloud_helper.get_products_vpn(params)
    if products_vpn.get('total_records') == 0:
        await bot.send_message(message.from_user.id, nav.WRONG, reply_markup = nav.mainMenu)
        return 1
    product = products_vpn.get('data')[0]
    server = product.get('server')
    # FIX ME - добавление в subscribers
    # FIX ME - запрос в python-backend, там подключение к серверу, генерацию ovpn, и отправку фаила
    await message.reply_document(open('file.ovpn', 'rb'))


executor.start_polling(dp, skip_updates = True)
