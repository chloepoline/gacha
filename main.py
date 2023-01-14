import random
import telebot
from telebot import types
import time

token = '5606392966:AAFdiNg16QwP-uNv5OgIE4ckmJDNTO-nH_o'
bot = telebot.TeleBot(token)
primogems = 0
distance_5_star = 0
distance_4_star = 0
rarities = ['⭐⭐⭐⭐⭐', '⭐⭐⭐⭐', '⭐⭐⭐']
items = {'⭐⭐⭐⭐⭐': ['Небесный атлас', 'Небесный меч', 'Небесное крыло'],
         '⭐⭐⭐⭐': ['Лунное сияние ксифоса', 'Ржавый лук'],
         '⭐⭐⭐': ['Рогатка', 'Филейный нож', 'Белая кисть', 'Металлическая тень']}

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Получить примогемы💎')
    btn2 = types.KeyboardButton('История')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text='Добро пожаловать в реролл банеров ', reply_markup=markup)

от

def reroll():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = 'Крутить 1 раз💫'
    btn2 = 'Крутить 10 раз💫'
    btn3 = 'Мои примогемы🔎'
    btn4 = 'Получить примогемы💎'
    markup.add(btn1, btn2, btn3, btn4)
    return markup

def info():
    #insert
    pass

def gacha(roll_count):
    global distance_5_star, distance_4_star, rarities
    drop = {'⭐⭐⭐⭐⭐': [], '⭐⭐⭐⭐': [], '⭐⭐⭐': []}
    for roll in range(roll_count):
        drop_star = random.choices(rarities, weights=[0.6, 5.1, 94.3])[0]

        if distance_5_star + 1 == 90 and (drop_star == '⭐⭐⭐⭐' or drop_star == '⭐⭐⭐'):
            drop_star = '⭐⭐⭐⭐⭐'
            distance_5_star = 0
        elif distance_4_star + 1 == 10 and (drop_star == '⭐⭐⭐'):
            drop_star = '⭐⭐⭐⭐'
            distance_4_star = 0
        elif drop_star == '⭐⭐⭐⭐⭐':
            distance_5_star = 0
        elif drop_star == '⭐⭐⭐⭐':
            distance_4_star = 0
            distance_5_star += 1
        elif drop_star == '⭐⭐⭐':
            distance_4_star += 1
            distance_5_star += 1

        drop[drop_star].append(random.choice(items[drop_star]))
    return drop

def form_mes(drop):
    # drop = {'⭐⭐⭐⭐⭐': [], '⭐⭐⭐⭐': [], '⭐⭐⭐': []}
    msg = ''
    if drop['⭐⭐⭐⭐⭐']:
        drop['⭐⭐⭐⭐⭐'] = ['⭐⭐⭐⭐⭐' + i for i in drop['⭐⭐⭐⭐⭐']]
        msg += '\n'.join(drop['⭐⭐⭐⭐⭐']) + '\n'
    if drop['⭐⭐⭐⭐']:
        drop['⭐⭐⭐⭐'] = ['⭐⭐⭐⭐' + i for i in drop['⭐⭐⭐⭐']]
        msg += '\n'.join(drop['⭐⭐⭐⭐']) + '\n'
    if drop['⭐⭐⭐']:
        drop['⭐⭐⭐'] = ['⭐⭐⭐' + i for i in drop['⭐⭐⭐']]
        msg += '\n'.join(drop['⭐⭐⭐'])

    return msg

@bot.message_handler(content_types=['text'])
def game_body(message):
    global primogems
    if message.text == 'Получить примогемы💎':
        primogems += 1600
        bot.send_message(message.chat.id, text='Теперь ты можешь покрутить', reply_markup=reroll())

    if message.text == 'Мои примогемы🔎':
        bot.send_message(message.chat.id, text=f'Примогемы: {primogems}')

    if message.text == 'Крутить 1 раз💫':
        if primogems >= 160:
            primogems -= 160
            drop = gacha(1)

            if drop['⭐⭐⭐⭐⭐']:
                animation = 'https://tenor.com/ru/view/genshin-impact-wish-genshin-legendary-orange-gif-26472706'
                photo = open(fr'img\{drop["⭐⭐⭐⭐⭐"][0]}.jpg', 'rb')
            elif drop['⭐⭐⭐⭐']:
                animation = 'https://tenor.com/ru/view/genshin-wish-genshin-impact-rare-purple-gif-26472708'
                photo = open(fr'img\{drop["⭐⭐⭐⭐"][0]}.jpg', 'rb')
            else:
                animation = "https://tenor.com/ru/view/genshin-impact-wish-common-gif-26472698"
                photo = open(fr'img\{drop["⭐⭐⭐"][0]}.jpg', 'rb')

            msg = bot.send_animation(message.chat.id, animation=animation)
            time.sleep(5.55)
            bot.delete_message(message.chat.id, msg.message_id)

            mes = form_mes(drop)
            bot.send_photo(message.chat.id, photo,
                           caption=f'{message.from_user.first_name}, тебе выпал:\n<b>{mes}</b>',
                           parse_mode='HTML')
            photo.close()
        else:
            bot.send_message(message.chat.id, text='Извините у вас не хватает примогемов', reply_markup=reroll())

    if message.text == 'Крутить 10 раз💫':
        if primogems >= 1600:
            primogems -= 1600
            drop = gacha(10)

            if drop['⭐⭐⭐⭐⭐']:
                animation = 'https://tenor.com/ru/view/genshin-impact-wish-genshin-legendary-orange-gif-26472706'
                photo = open(fr'img\{drop["⭐⭐⭐⭐⭐"][0]}.jpg', 'rb')
            elif drop['⭐⭐⭐⭐']:
                animation = 'https://tenor.com/ru/view/genshin-wish-genshin-impact-rare-purple-gif-26472708'
                photo = open(fr'img\{drop["⭐⭐⭐⭐"][0]}.jpg', 'rb')
            else:
                animation = "https://tenor.com/ru/view/genshin-impact-wish-common-gif-26472698"
                photo = open(fr'img\{drop["⭐⭐⭐"][0]}.jpg', 'rb')

            msg = bot.send_animation(message.chat.id, animation=animation)
            time.sleep(5.55)
            bot.delete_message(message.chat.id, msg.message_id)

            mes = form_mes(drop)
            bot.send_photo(message.chat.id, photo,
                           caption=f'{message.from_user.first_name}, тебе выпали:\n<b>{mes}</b>',
                           parse_mode="HTML")
            photo.close()
        else:
            bot.send_message(message.chat.id, text='Извините у вас не хватает примогемов', reply_markup=reroll())

bot.polling(non_stop=True)
