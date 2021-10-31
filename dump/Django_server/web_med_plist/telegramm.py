import telepot 
import json
import asyncio
import requests
import time
import urllib
from PIL import Image
from telethon import TelegramClient
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from telethon.tl.functions.photos import UploadProfilePhotoRequest
import os
import environ
env = environ.Env()
environ.Env.read_env()


token2 = '1592191687:AAELJBeFjw0mmEP4nVSno2O3neyxFeO0qAE'
my_id_2 = ''
token = '981018030:AAG91YfH_rVfHWghCP9KZLyT_CkHEw-mQwU'
my_id = 1087524368

telegramBot = telepot.Bot(token)
# https://api.telegram.org/bot981018030:AAG91YfH_rVfHWghCP9KZLyT_CkHEw-mQwU/getMe
URL = "https://api.telegram.org/bot{}/".format(token)


def send_message(text):
    telegramBot.sendMessage(
        my_id, text, parse_mode="Markdown")


# def send_message_user(text):
#     telegramBot.sendMessage(
#         '@plavrentev2010', text, parse_mode="Markdown")


# def get_url(url):
#     response = requests.get(url)
#     content = response.content.decode("utf8")
#     return content


# def send_message2(text, chat_id):
#     text = urllib.parse.quote_plus(text)
#     url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
#     get_url(url)


def telegram_bot_sendtext(bot_message):

    bot_token = token
    bot_chatID = str(my_id)
    send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message # noqa
    response = requests.get(send_text)

    return response.json()


# test = telegram_bot_sendtext('Testing Telegram bot')
# print(test)

# send message appointment user
# sender's phone number
phone_number = '79955946880'
# recievers phone number
guest_phone_number = '79041164527'
text_message_telegram = 'Привет это твой бот, \
    проверка связи avatar username NEWWWVIPCILIA '

api_id = os.environ.get('APP_API_AD_TELEGRAM_JS_CILIA')
api_hash = os.environ.get('APP_API_HASH_TELEGRAM_JS_CILIA')
login_79041164527 = os.environ.get('LOGIN_BOT_SENDER_TELEGRAM_JS_CILIA')
name_user_phone_79041164527 = os.environ.get(
    'NAME_USER_SENDER_TELEGRAM_79041164527')


def send_massage_telegram_user_appointment(
    phone_number,
    guest_phone_number,
    text_message_telegram):

    # img_avatar_telegram = Image.open(
    #     "./static/images/img_avatar_telegram.png")
    client = TelegramClient(
        'session_name',
        api_id,
        api_hash)

    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone_number)
        me = client.sign_in(phone_number, input('Enter code: ')) # noqa
        # https://question-it.com/questions/1705826/avtomaticheskij-vhod-v-klient-telegram-s-pomoschju-telethon-python


    image_bot = client.upload_file('./static/images/img_avatar_telegram.png')
    client(UploadProfilePhotoRequest(image_bot))

    # ---------------------------------------
    # add user to contact
    contact = InputPhoneContact(
        client_id=0,
        phone=guest_phone_number,
        first_name=login_79041164527, last_name=name_user_phone_79041164527)
    result = client.invoke(ImportContactsRequest([contact]))
    # ---------------------------------------
    # send message to reciever
    client.send_message(result.users[0], text_message_telegram)
