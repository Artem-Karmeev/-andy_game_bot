from aiogram import types
from aiogram.dispatcher.filters import Text
from random import randint as rnt
from config import dp
from my_bot import my_bot

from text import text_1

count_candy = 0
fate = 0


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'Приветствую тебя, {message.from_user.first_name}!\n \n/game - Начать игру 🎮  \n/help - Читать правила 👀')


@dp.message_handler(commands=['help'])
async def start(message: types.Message):
    await message.answer(text_1)


@dp.message_handler(commands=['game'])
async def start(message: types.Message):
    global count_candy
    global fate
    fate = rnt(0,1)
    count_candy = 150
    await message.answer(f'\nДа начнутся голодные игры!\n На столе лежит 150 конфет')
    if fate:
        await message.answer(f'По итогам жеребьевки, первый ход за тобой 🫵, сколько возьмешь 🍬? ')
    else:
        await message.answer(f'По итогам жеребьевки, первым ходит бот')
        num = my_bot(count_candy)
        count_candy -= num
        await message.answer(f'Бот взял {num} 🍬, на столе осталось {count_candy} 🍬.')


@dp.message_handler()
async def mes_all(message: types.Message):
    global count_candy
    global fate

    if count_candy > 0:

        if message.text.isdigit(): 
            if 0 < int(message.text) < 29:
                count_candy -= int(message.text)
                if count_candy > 0:
                    await message.answer(f'На столе осталось {count_candy} 🍬')
                    num = my_bot(count_candy)
                    count_candy -= num
                    if count_candy > 0:
                        await message.answer(f'Бот взял {num} 🍬, на столе осталось {count_candy} 🍬. \nСколько возьмешь конфет?')
                    else:

                        await message.answer('... и их забрал бот! \nПобедил бот 🤖, грядет восстание машин!')
                else:
                    await message.answer(f'{message.from_user.first_name} одерживает победу🏆!')
            else:
                await message.answer('За раз можно взять не более 28 конфет!')
        else:
            await message.answer(f'Не понял, повтори')
    else:
        await message.answer('На столе нет конфет. \nЧтобы начать играть жми /game ')





