import telebot

from my_bot import my_bot

bot = telebot.TeleBot('5977832137:AAH1GqA90JF4Qef4fAKqSMNQflQEWrASJzs')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, добро пожаловать! \n\
        \nВведи /game чтобы начать игру. \nВведи /help чтобы смотреть правила.')

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, f'На столе лежит 2021 конфета. \n \
Играют два игрока делая ход друг после друга.\n\
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n\
Все конфеты оппонента достаются сделавшему последний ход.\n \
Чтобы преждевременно завершить игру введи /start')

@bot.message_handler(commands=['game'])
def my_input(message):
    step = bot.send_message(message.chat.id, 'Твой ход:')
    bot.register_next_step_handler(step, verify)

def verify(message):

    if int(message.text.isdigit()):
        if 0 < int(message.text) < 29: 
            sum_candy -= (message.text)
            bot.send_message(message.chat.id, f'Осталось {sum_candy} конфет.')
            
        else:
            bot.send_message(message.chat.id, 'Нужно ввести число от 1 до 28')
            my_input(message)
    else:
        bot.send_message(message.chat.id, 'только число')
        my_input(message)

def game(message):



bot.polling(non_stop=True)