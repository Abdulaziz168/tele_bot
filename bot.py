import telebot
from telebot import types
from flask import Flask, request
from telegram.ext import updater
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))

token = '5168803436:AAEWQv22YopYjK7aH-YVgh2XBk4y9Ruej8s'
bot = telebot.TeleBot(token)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Assalomu alaykum Sevimliplay playformasi botiga xush kelibsiz')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("To‘lov qanday qilinadi")
    item2 = types.KeyboardButton("Video qo'llanma")
    item3 = types.KeyboardButton("admin bilan aloqa  **@SSerIouSS**")
    item4 = types.KeyboardButton("savollar")

    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Menu Tanlang', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Video qo'llanma":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=A1p7bEtTlxc")
    elif message.text == "To‘lov qanday qilinadi":
        bot.send_message(message.chat.id, '''“Sevimli play” platformasi oʻz faoliyatini pullik tizimda davom ettiradi. Turkiya seriallarini toʻliq tomosha qilish uchun oylik abonent toʻlovi 11 000 soʻm. 
Yangi tizimdan foydalanish uchun:
1. Mobil qurilma yoki kompyuter brauzeri orqali www.sevimliplay.tv saytiga kiriladi.
2. Kirish tugmasi bosiladi, login-parol terib, akkautga kiriladi.
3. Obunalar boʻlimiga oʻtib, karta orqali 11 000 soʻm toʻlanadi.
4. Jarayon tugagach, ilovaga qayta kirib, 1 oy davomida platformadan toʻliq foydalansa bo‘ladi!''')


updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=token)

updater.bot.setWebhook('https://afternoon-eyrie-49069.herokuapp.com/' + token)

bot.infinity_polling()
