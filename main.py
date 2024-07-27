from config import token
from fistPower import first_power
from registrationNewUser import registration_new_user

import telebot

bot = telebot.TeleBot(token)

dict_users = first_power()


@bot.message_handler(commands=['start'])
def start_tg_bot(message):
    user_id = str(message.chat.id)
    dict_users[user_id] = registration_new_user(user_id)

    pass

