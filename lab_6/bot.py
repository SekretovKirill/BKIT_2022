import telebot
import random
from telebot import types
bot = telebot.TeleBot('INSERT TOKEN')
user_list=[]



def roll(mod):
    a=[128526, 127814, 127826, 128081, 128701, 128574, 128181, 128186]
    first = '| '+chr(random.choice(a))+' | '+chr(random.choice(a))+' | '+chr(random.choice(a))+' | '
    second = '| '+chr(random.choice(a)) + ' | ' + chr(random.choice(a)) + ' | ' + chr(random.choice(a))+' | '
    third = '| '+chr(random.choice(a)) + ' | ' + chr(random.choice(a)) + ' | ' + chr(random.choice(a))+' | '
    b=[first, second, third]
    fin=0
    for i in b:
        print(i, '/n')
        if '| 😎 | 😎 | 😎 |' in i:
            fin += 500 * mod
        elif '| 👑 | 👑 | 👑 |' in i:
            fin += 100 * mod
        elif '| 🍆 | 🍆 | 🍆 |' in i:
            fin += 75 * mod
        elif '| 🍒 | 🍒 | 🍒 |' in i:
            fin += 50 * mod
        elif '| 💵 | 💵 | 💵 |' in i:
            fin += 25 * mod
        elif '| 😾 | 😾 | 😾 |' in i:
            fin += 15 * mod
        elif '| 💺 | 💺 | 💺 |' in i:
            fin += 10 * mod
        elif '| 🚽 | 🚽 | 🚽 |' in i:
            fin += 5 * mod
        elif '| 🚽 | 🚽 |' in i or i.count('| 🚽 |')==2:
            fin += 2 * mod
    return fin, first, second, third
#print(roll(1),chr(128526), chr(127814), chr(127826), chr(128081), chr(128701), chr(128574), chr(128181), chr(128186))


@bot.message_handler(commands=['start'])
def priv(message):
    if message.from_user.id not in user_list:
        user_list.append(message.from_user.id)
        print(user_list)
        data='play'+'|'+'300'
        keyboard = types.InlineKeyboardMarkup()
        callback_button = types.InlineKeyboardButton(text="Начать подъем $$$", callback_data=data)
        keyboard.add(callback_button)
        bot.reply_to(message, '''Приветствую {first} \nЯ - бот к̶а̶з̶и̶н̶о̶ веселые картинки с денежной ставкой \nДля начала игры нужно нажать на кнопку с размером ставки \nПриветственный бонус: 100руб'''.format(first=message.from_user.first_name))
        bot.send_message(message.chat.id,'\nСписок победных комбинаций: \n|😎|😎|😎| X 500\n|👑|👑|👑| X 100\n|🍆|🍆|🍆| X 75\n|🍒|🍒|🍒| X 50\n|💵|💵|💵| X 25\n|😾|😾|😾| X 15\n|💺|💺|💺| X 10\n|🚽|🚽|🚽| X 5\n|🚽|🚽|🔯| X 2\n🔯-любой символ', reply_markup=keyboard)
        print('first')



@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.from_user.id not in user_list:
        bot.send_message(call.from_user.id, 'Для начала работы с ботом напишите /start')
        return
    data = call.data.split('|')[0]
    money = call.data.split('|')[1]
    if data == 'play':
        keyboard = types.InlineKeyboardMarkup()
        main='main|'+str(money)
        one='one|'+str(money)
        two = 'two|'+str(money)
        five = 'five|'+str(money)
        callback_button = types.InlineKeyboardButton(text="помощь", callback_data=main)
        callback_one = types.InlineKeyboardButton(text="Спин 1руб", callback_data=one)
        callback_two = types.InlineKeyboardButton(text="Спин 2руб", callback_data=two)
        callback_five = types.InlineKeyboardButton(text="Спин 5руб", callback_data=five)
        keyboard.add(callback_one, callback_two, callback_five, callback_button)
        bot.send_message(call.message.chat.id, 'Ну что, начинаем🥶🥶🥶??\nТвой балланс: {money}руб'.format(money=money),reply_markup=keyboard)
    elif data =='main':
        keyboard = types.InlineKeyboardMarkup()
        play='play|'+str(money)
        callback_play = types.InlineKeyboardButton(text="Начать подъем $$$ \n", callback_data=play)
        keyboard.add(callback_play)
        bot.send_message(call.message.chat.id, '''Я - бот к̶а̶з̶и̶н̶о̶ веселые картинки с денежной ставкой \nДля начала игры нужно нажать на кнопку с размером ставки\nТвой балланс: {money}руб'''.format(money=money))
        bot.send_message(call.message.chat.id, '\nСписок победных комбинаций: \n|😎|😎|😎| X 500\n|👑|👑|👑| X 100\n|🍆|🍆|🍆| X 75\n|🍒|🍒|🍒| X 50\n|💵|💵|💵| X 25\n|😾|😾|😾| X 15\n|💺|💺|💺| X 10\n|🚽|🚽|🚽| X 5\n|🚽|🚽|🔯| X 2\n|🚽|🔯|🔯| X 1\n🔯-любой символ', reply_markup=keyboard)
    elif data == 'one':
        ko=1
        numb(data, money, ko, call)
    elif data == 'two':
        ko = 2
        numb(data, money, ko, call)
    elif data == 'five':
        ko = 5
        numb(data, money, ko, call)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
def numb(data, money, ko, call):
    money = int(money)
    kol, first, second, third = roll(ko)
    nmoney = money
    if money -ko+kol<=0:
        money=0
        keyboard = types.InlineKeyboardMarkup()
        main = 'main|' + str(money)
        callback_button = types.InlineKeyboardButton(text="помощь", callback_data=main)
        keyboard.add(callback_button)
        print(money)
        bot.send_message(call.message.chat.id, 'АХАХААХА деньги кончились😂😂😂 Донать мне в вк😎😎😎', reply_markup=keyboard)
        return
    money = money - ko + kol
    win = '-'
    if nmoney>money:
        luck = 'Неудача 😖 Попробуй еще!'
    else:
        luck = 'Победа 🤩🤩🤩'
        win = money - nmoney

    keyboard = types.InlineKeyboardMarkup()
    main='main|'+str(money)
    one='one|'+str(money)
    two = 'two|'+str(money)
    five = 'five|'+str(money)
    print(money)
    callback_button = types.InlineKeyboardButton(text="помощь", callback_data=main)
    callback_one = types.InlineKeyboardButton(text="Спин 1руб", callback_data=one)
    callback_two = types.InlineKeyboardButton(text="Спин 2руб", callback_data=two)
    callback_five = types.InlineKeyboardButton(text="Спин 5руб", callback_data=five)
    keyboard.add(callback_one, callback_two, callback_five, callback_button)
    bot.send_message(call.message.chat.id,
                     '{luck}\n\n{first}     Ставка: {ko}\n{second}     Выигрыш: {win}\n{third}     Баланс: {money}'.format(ko = ko, win = win, money=money, first=first, second=second,
                                                                            third=third, luck=luck), reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Че здороваешься, слоты не ждут 💵💵💵')
    if message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'Пока, но я знаю, что ты вернешься 😉')

bot.polling(none_stop=True)
