import telebot
from telebot import types
from flask import Flask, request

token = '5168803436:AAEWQv22YopYjK7aH-YVgh2XBk4y9Ruej8s'
bot = telebot.TeleBot(token)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Assalomu alaykum Sevimliplay playformasi botiga xush kelibsiz')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("To‘lov qanday qilinadi")
    item2 = types.KeyboardButton("Video qo'llanma")
    item3 = types.KeyboardButton("admin bilan aloqa ")
    item4 = types.KeyboardButton("photo")
    markup.row(item1, item2)
    markup.row(item3, item4)

    bot.send_message(message.chat.id, 'Menu Tanlang', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == "Video qo'llanma":
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=XnzxEGLaPxs")
    elif message.text == "photo":
        photo = open("pay.jpg", 'rb')
        bot.send_photo(message.chat.id ,photo)
    elif message.text == "admin bilan aloqa":
        bot.send_message(message.chat.id, "Adminimiz bilan bog‘laning @Rejissor_shaxzod_official ")
    elif message.text == "To‘lov qanday qilinadi":
        bot.send_message(message.chat.id, '''“Sevimli play” platformasi oʻz faoliyatini pullik tizimda davom ettiradi. Turkiya seriallarini toʻliq tomosha qilish uchun oylik abonent toʻlovi 11 000 soʻm. 
Yangi tizimdan foydalanish uchun:
1. Mobil qurilma yoki kompyuter brauzeri orqali www.sevimliplay.tv saytiga kiriladi.
2. Kirish tugmasi bosiladi, login-parol terib, akkautga kiriladi.
3. Obunalar boʻlimiga oʻtib, karta orqali 11 000 soʻm toʻlanadi.
4. Jarayon tugagach, ilovaga qayta kirib, 1 oy davomida platformadan toʻliq foydalansa bo‘ladi!''')


def get_locations(message):
    bot.send_contact()


bot.infinity_polling()
