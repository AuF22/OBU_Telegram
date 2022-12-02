import random
import telebot
import time
import sqlite3
from fuzzywuzzy import fuzz
from telebot import types
from tg2 import PLAN, praise, ACTIV, b, f404, PROVODKI
my = 492697956

db = sqlite3.connect('ID.db', check_same_thread=False)
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS id2 (
ID TEXT,
USERS TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS admins (
AD_ID TEXT, 
USER TEXT
)""")
db.commit()

sql.execute("""CREATE TABLE IF NOT EXISTS wiring (wir TEXT)""")
db.commit()



def rec(message):
    answer = message.text
    for user in sql.execute('SELECT * FROM id2 ORDER BY USERS'):
        try:
            user = user[0]
            user = str(user)
            user = int(user)
            bot.send_message(message.chat.id, user)
            bot.send_message(user, answer)
        except:
            bot.send_message(message.chat.id, 'У чела новый айди')

t = 0
tr = 0
fl = 0
s_t = 0
s_tr = 0
s_fl = 0
b_game = 'Игра 🎲'
search = 'Поиск 🔍'

def add_wir(message):
    answer = message.text
    try:
        sql.execute(f"SELECT wir FROM wiring WHERE wir = '{answer}' ")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO wiring VALUES (?)", (answer,))
            db.commit()
            bot.send_message(message.chat.id, f'Проводка:\n{answer}\nУспешно добавлена!')
            bot.send_message(message.chat.id, 'Введите следующую проводку!')
    except:
        bot.send_message(message.chat.id, 'Проводка не добавлена')

def prov(message, P, proc=75):
    c = 0

    for i in P:
        a = fuzz.partial_ratio(message.text, str(i))
        if int(a) >= proc:
            bot.send_message(message.chat.id, i)
            c += 1
            time.sleep(0.2)
    if c == 0:
        bot.reply_to(message, f404)

def t_prov(message, P, proc = 85):
    c = 0
    for i in P:
        a = fuzz.partial_ratio(message.text, i)
        if int(a) >= proc:
            bot.send_message(message.chat.id, i)
            c += 1
            time.sleep(0.2)
    if c == 0:
        bot.reply_to(message, f404)

def termin(message):
    cr = []
    ab = 0
    tt = open('ter.txt', encoding='utf8')
    for line in tt:
        cr.append(line)
    tt.close()
    t_prov(message, cr, proc=85)
    #запускает старт "игры"

def s_gm(message):
    s_testing()
    global s_r
    s_r = []

    r_random(s_test, s_r)

    s_gmb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    s_gmb.add(
        types.KeyboardButton(s_test[s_r[0]][0]),
        types.KeyboardButton(s_test[s_r[1]][0]),
        types.KeyboardButton(s_test[s_r[2]][0]),
        types.KeyboardButton(s_test[s_r[3]][0]),
        types.KeyboardButton(b)
    )
    global s_rk
    s_rk = random.randint(0, 3)

    bot.send_message(message.chat.id, s_test[s_r[s_rk]][1], reply_markup=s_gmb)
    bot.register_next_step_handler(message, s_game)


def gm(message):
    testing()
    global r
    r = []

    r_random(test, r)

    gmb = types.ReplyKeyboardMarkup(resize_keyboard=False)
    gmb.add(
        types.KeyboardButton(test[r[0]][1]),
        types.KeyboardButton(test[r[1]][1])
    )
    gmb.add(
        types.KeyboardButton(test[r[2]][1]),
        types.KeyboardButton(test[r[3]][1])
    )

    gmb.add(types.KeyboardButton(b))
    global rk
    rk = random.randint(0, 3)

    bot.send_message(message.chat.id, test[r[rk]][0], reply_markup=gmb)

    bot.register_next_step_handler(message, game)
    #запуск старта


def adm_st2(message):
    adm_b2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm_b2.add(
        types.KeyboardButton('Admins'),
        types.KeyboardButton('Admins.D'),

    )
def adm_st(message):

    adm_botton = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm_botton.add(
        types.KeyboardButton('Реклама 📺'),
        types.KeyboardButton('Пользователи 👱🏼‍♂️'),
        types.KeyboardButton('Admin.add 🙋🏻‍♂️'),
        types.KeyboardButton('Проводки.add ✉️'),
        types.KeyboardButton(b),
        types.KeyboardButton('Next')
    )

    bot.send_message(message.chat.id, 'Вы вошли в ADMIN панель', reply_markup=adm_botton)
def adm_2(message):
    adm_botton = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    adm_botton.add(
        types.KeyboardButton('Реклама 📺'),
        types.KeyboardButton('Пользователи 👱🏼‍♂️'),
        types.KeyboardButton('Проводки.add ✉️'),
        types.KeyboardButton(b)
    )

    bot.send_message(message.cgat.id, 'Вы вошли в ADMIN панель', reply_markup=adm_botton)

def st(message):

    button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button.add(
        types.KeyboardButton('Счета 🧮'),
        types.KeyboardButton('Проводки 📝'),
        types.KeyboardButton('Термины 🎓'),
        types.KeyboardButton('Информация ℹ️')
    )
    bot.send_message(message.chat.id, '⏹ Вы находитесь в главном меню ', reply_markup=button)
    #сам лист с вопросами

#создаю лист для вопросов проводки
def testing():
    for i in PROVODKI:
        a = i.split('\n', 1)
        test.append(a)

test = []
r = []#рандомный ответ
rk = 0
s_r = []
s_rk = 0

def s_testing():
    for i in PLAN:
        a = i.split(':')
        s_test.append(a)

s_test = []

def r_random(a, r):
    while len(r) < 4:
        x = random.randint(0, len(a) - 1)
        if x not in r:
            r.append(x)

bot = telebot.TeleBot("1716157591:AAFvuQbsG26fFZRTpyzrHJf7ACuSpQ6_Qkg")

@bot.message_handler(commands=['admin'])
def admin(message):
    ida = message.chat.id
    if ida == my:
        adm_st(message)
    else:
        c = 0
        for admins in sql.execute('SELECT AD_ID FROM admins'):
            if admins == str(ida):
                c += 1
                adm_2(message)
            else:
                continue
        if c == 0:
            bot.send_message(message.chat.id, 'У вас нет прав на это действие!')

@bot.message_handler(commands=['start'])
def start(message):

    id = message.chat.id
    id = str(id)

    user_name = message.from_user.username
    try:

        sql.execute(f"SELECT ID FROM id2 WHERE ID = '{id}' ")
        if sql.fetchone() is None:
            sql.execute(f"INSERT INTO id2 VALUES (?, ?)", (id, user_name,))
            db.commit()
            bot.send_message(my, f'Новый пользователь @{message.from_user.username}')
    except:
        bot.send_message(my, 'Что-то не так')


    bot.reply_to(message, "Справочник по ОБУ,  помогу чем смогу")
    st(message)

def users(message):
    c = 0
    try:
        for user in sql.execute('SELECT * FROM id2 ORDER BY USERS'):
            c += 1
            try:
                bot.send_message(message.chat.id, '@' + user[1])
            except:
                pass

        bot.send_message(message.chat.id, f'Число юзеров: {c}')
    except:
        bot.send_message(message.chat.id, 'Что-то не так!')

@bot.message_handler(commands=['top'])
def top(message):
    bot.send_message(message.chat.id, 'Раз вы уже сюда дошли')
    bot.send_message(message.chat.id, '''Разработчик: Асеев Алтынбек
Псевдоним: AuF
Группа: Бух 1-19
Instagram: https://www.instagram.com/mr_aseev14/ ''' )
    bot.send_message(message.chat.id, 'Теперь вы знаете чуть бльше обо мне)')
    st(message)

@bot.message_handler(commands=['rs'])
def rs(message):
    global t
    global s_t
    global tr
    global s_tr
    global fl
    global s_fl
    t = 0
    s_t = 0
    tr = 0
    s_tr = 0
    fl = 0
    s_fl = 0
    bot.send_message(message.chat.id, 'Идет процесс сброса...')
    a = random.randint(1, 40)
    bot.send_message(message.chat.id, 'Сброс произошел на ' + str(a) + '%')
    time.sleep(0.6)
    b = random.randint(40, 80)
    bot.send_message(message.chat.id, 'Сброс произошел на ' + str(b) + '%')
    time.sleep(0.9)
    c = random.randint(80, 99)
    bot.send_message(message.chat.id, 'Сброс произошел на ' + str(c) + '%')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Сброс произошел на 100%!')
    bot.send_message(message.chat.id, 'Успешно!')
    st(message)

@bot.message_handler(commands=['menu'])
def menu(message):
    st(message)

@bot.message_handler(commands=['lesson'])
def lesson_OBU(message):
    IN_button = types.InlineKeyboardMarkup(row_width=4)
    IN_button.add(
        types.InlineKeyboardButton('Урок 1', url='https://www.youtube.com/watch?v=j-QYFJJRp9M&ab'),
        types.InlineKeyboardButton('Урок 2', url='https://www.youtube.com/watch?v=YqD30F_5m2Q&ab'),
        types.InlineKeyboardButton('Урок 3', url='https://www.youtube.com/watch?v=DMO7DP31-AU&ab'),

        types.InlineKeyboardButton('Урок 4', url='https://www.youtube.com/watch?v=oGh_K-aCYTU&ab'),
        types.InlineKeyboardButton('Урок 5',url='https://www.youtube.com/watch?v=CkGMlLv0YTA&ab'),
        types.InlineKeyboardButton('Урок 6', url='https://www.youtube.com/watch?v=6N_C2NhNMPQ'),

        types.InlineKeyboardButton('Урок 7', url='https://www.youtube.com/watch?v=P7g4T_5364s'),
        types.InlineKeyboardButton('Урок 8', url='https://www.youtube.com/watch?v=fvziqAYwYPE'),
        types.InlineKeyboardButton('Урок 9', url='https://www.youtube.com/watch?v=-oq8UCkAo70'),

        types.InlineKeyboardButton('Урок 10', url='https://www.youtube.com/watch?v=2ukt4bUQMV4'),
        types.InlineKeyboardButton('Урок 11', url='https://www.youtube.com/watch?v=RJ8kTaGOIb8'),
        types.InlineKeyboardButton('Урок 12', url='https://www.youtube.com/watch?v=xZ_2VpaHi-A'),

        types.InlineKeyboardButton('Урок 13', url='https://www.youtube.com/watch?v=mXTS0VNJL4k'),
        types.InlineKeyboardButton('Урок 14', url='https://www.youtube.com/watch?v=jGjr2mCslQU'),
        types.InlineKeyboardButton('Урок 15', url='https://www.youtube.com/watch?v=SFagibuUVkk'),

        types.InlineKeyboardButton('Урок 16', url='https://www.youtube.com/watch?v=POtC4zyruu0'),
        types.InlineKeyboardButton('Урок 17', url='https://www.youtube.com/watch?v=H3Ofc9B0R_I'),
        types.InlineKeyboardButton('Урок 18', url='https://www.youtube.com/watch?v=Sq5-xylAOno'),

        types.InlineKeyboardButton('Урок 19', url='https://www.youtube.com/watch?v=XhVMlcAr8Yo'),
        types.InlineKeyboardButton('Урок 20', url='https://www.youtube.com/watch?v=wFRcifSCUJo'),
        types.InlineKeyboardButton('Урок 21', url='https://www.youtube.com/watch?v=qWreUpqzZp0'),

        types.InlineKeyboardButton('Урок 22', url='https://www.youtube.com/watch?v=9e7A3qBqT1k'),
        types.InlineKeyboardButton('Урок 23', url='https://www.youtube.com/watch?v=stNJYqVALQc')
    )

    bot.send_message(message.chat.id, 'Уроки по ОБУ:', reply_markup=IN_button)
    st(message)

def lesson_POBUA(message):
    in_button = types.InlineKeyboardMarkup()
    in_button.add(
        types.InlineKeyboardButton('Урок 1', url='https://www.youtube.com/watch?v=XyOy3ypgBo4&t=9s')
    )
    in_button.add(
        types.InlineKeyboardButton('ОБУ', callback_data='OBU')
    )
    bot.send_message(message.chat.id, 'Уроки по ПОБУА', reply_markup=in_button)

@bot.message_handler(content_types=['text', "photo"])
def check(message):
    id_u = message.chat.id

    if message.text == 'Реклама 📺':
        sql.execute(f"SELECT AD_ID FROM admins WHERE AD_ID = '{id_u}' ")
        if id_u == my:
            bot.send_message(my, 'Введите рекламу')
            bot.register_next_step_handler(message, reclaim)

        elif sql.fetchone() is None:
            bot.send_message(message.chat.id, "У вас нет прав на это действие")
            st(message)
        elif id_u == my:
            bot.send_message(my, 'Введите рекламу')
        else:
            bot.send_message(message.chat.id, 'Введите рекламу')
            bot.register_next_step_handler(message, reclaim)

    elif message.text == 'Пользователи 👱🏼‍♂️':
        sql.execute(f"SELECT AD_ID FROM admins WHERE AD_ID = '{id_u}' ")
        if id_u == my:
            users(message)
            adm_st(message)
        elif sql.fetchone() is None:
            bot.send_message(message.chat.id, "У вас нет прав на это действие")
            st(message)
        else:
            users(message)
            adm_2(message)
    elif message.text == 'Проводки.add ✉️':
        sql.execute(f"SELECT AD_ID FROM admins WHERE AD_ID = '{id_u}'")
        if id_u == my:
            bot.send_message(message.chat.id, 'Введите проводку для добавления!')
            bot.register_next_step_handler(message, add_wiring)





    elif message.text == 'Счета 🧮':
        s_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s_button.add(
            types.KeyboardButton(search),
            types.KeyboardButton(b_game),
            types.KeyboardButton('Справка по счетам 🧾'),
            types.KeyboardButton(b)
        )
        bot.send_message(message.chat.id, 'Хочешь найти счет или проверить свои знания ?\nРешайся:', reply_markup=s_button)
        bot.register_next_step_handler(message, score)

    elif message.text == 'Проводки 📝':
        w_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        w_button.add(
            types.KeyboardButton(search),
            types.KeyboardButton(b_game),
            types.KeyboardButton(b)
        )
        bot.send_message(message.chat.id, 'Ты тут найдешь готовые проводки, или же сможешь проверить свои знания на составления проводок.', reply_markup=w_button)

        bot.register_next_step_handler(message, wiring)

    elif message.text == 'Термины 🎓':
        t_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        t_button.add(types.KeyboardButton(b))
        bot.send_message(message.chat.id, 'Введите термин', reply_markup=t_button)
        bot.register_next_step_handler(message, termins)

    elif message.text == 'Информация ℹ️':
        i_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        i_button.add(
            types.KeyboardButton('Обратная связь 👨🏻‍💻'),
            types.KeyboardButton('Информация ℹ️'),
            types.KeyboardButton(b)
        )
        bot.send_message(message.chat.id, '''Тут бесполезная Инфа, но если хочешь можешь поговорить со мной.
Потыкай на всё подряд 🙃''', reply_markup=i_button)
        bot.register_next_step_handler(message, information)

#блок (Счета)
def score(message):
    if message.text == b:
        st(message)
    elif message.text == search:
        bot.send_message(message.chat.id, 'Введите номер или название счета:')
        bot.register_next_step_handler(message, scores)
    elif message.text == 'Справка по счетам 🧾':
        bot.send_message(message.chat.id, ACTIV)
        bot.register_next_step_handler(message, score)
    elif message.text == b_game:
        s_gm(message)
def scores(message):
    if message.text == b:
        st(message)
    elif message.text == search:
        bot.reply_to(message, 'Вы уже ищите, не надо спамить 😡')
        bot.register_next_step_handler(message, scores)
    elif message.text == 'Справка по счетам 🧾':
        bot.send_message(message.chat.id, ACTIV)
        bot.register_next_step_handler(message, scores)
    elif message.text == b_game:
        s_gm(message)
    else:
        prov(message, sql.execute("SELECT pll FROM plan"), proc=90)
        bot.register_next_step_handler(message, scores)
def s_game(message):
    if message.text != b:
        try:
            global s_t
            s_t += 1
            if message.text == s_test[s_r[s_rk]][0]:
                global s_tr
                s_tr += 1
                bot.send_message(message.chat.id, '✅ Правильно\n' + praise[random.randint(0, len(praise) - 1)] + '\nСледующий счет:')
                time.sleep(0.1)
                s_gm(message)
            elif message.text == b:
                st(message)

            else:
                global s_fl
                s_fl += 1
                bot.send_message(message.chat.id, '❌ Неправильно! \n\n✅ Правильнее:\n\n' + s_test[s_r[s_rk]][0] + '\n\nСледующий счет:')
                time.sleep(0.1)
                s_gm(message)
        except:
            bot.send_message(message.chat.id, 'Упс что - то пошло не так перезапустите бота, и скажите разрабу!')
    elif message.text == b:
        s_button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        s_button.add(
            types.KeyboardButton(search),
            types.KeyboardButton(b_game),
            types.KeyboardButton('Справка по счетам 🧾'),
            types.KeyboardButton(b)
        )
        try:
            accuracy = ((s_tr/s_t)*100)
            accuracy = round(accuracy, 1)
        except:
            accuracy = 0
        bot.send_message(message.chat.id, f'⚠️Попыток: {s_t}\n\n✅ Правильно: {s_tr}\n\n❌ Неправильно: {s_fl}\n\n🎯 Т\
очность: {accuracy}%')

        bot.send_message(message.chat.id, 'Хочешь найти счет или проверить свои знания ?\nРешайся:', reply_markup=s_button)
        bot.register_next_step_handler(message, score)

# один блок (Проводок)
def wiring(message):

    if message.text == search:
        bot.send_message(message.chat.id, 'Введите проводку')
        bot.register_next_step_handler(message, wirings)
    elif message.text == b_game:
        gm(message)
    elif message.text == b:
        st(message)
def wirings(message):
    if message.text == b_game:
        gm(message)
    elif message.text == b:
        st(message)
    elif message.text == search:
        bot.reply_to(message, 'Вы уже ищите, не надо спамить 😡')
        bot.register_next_step_handler(message, wirings)
    else:
        prov(message, sql.execute("SELECT wir FROM wiring"))
        bot.register_next_step_handler(message, wirings)
def game(message):
    if message.text != b:
        try:
            global t
            t += 1
            if message.text == test[r[rk]][1]:
                global tr
                tr += 1
                bot.send_message(message.chat.id, '✅ Правильно\n' + praise[random.randint(0, len(praise) - 1)] + '\nСледующая проводка:')
                time.sleep(0.1)
                gm(message)
            else:
                global fl
                fl += 1
                bot.send_message(message.chat.id, '❌ Неправильно! \n\n✅ Правильнее:\n' + test[r[rk]][1] + '\n\nСледующая проводка:')
                time.sleep(0.1)
                gm(message)
        except:
            bot.send_message(message.chat.id, 'Упс что - то пошло не так перезапустите бота, и скажите разрабу!')
    elif message.text == b:
        w_button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        w_button.add(
            types.KeyboardButton(search),
            types.KeyboardButton(b_game),
            types.KeyboardButton(b)
        )
        try:
            accuracy = (tr/t)*100
            accuracy = round(accuracy, 1)
        except:
            accuracy = 0
        bot.send_message(message.chat.id, f'⚠️Попыток: {t}\n\n✅ Правильно: {tr}\n\n❌ Неправильно: {fl}\n\n🎯 Т\
очность: {accuracy}%')
        bot.send_message(message.chat.id, 'Ты тут найдешь готовые проводки, или же сможешь проверить свои знания на сос\
тавления проводок.', reply_markup=w_button)

        bot.register_next_step_handler(message, wiring)

#блок Инструкция
def information(message):
    if message.text == 'Информация ℹ️':
        bot.send_message(message.chat.id, '''Бот создан не экспертом по Бухгалтерскому учету.
За правильность проводок ответственности не несу.

Я лишь такой же студент, как и вы. Пытаясь облегчить свою учебу пришла мысль о создании этого бота, не судим стр\
ого. Ну вот и я решил поделится им с вами.  Он не идеален и поэтому прошу у вас помощи довести его до идеала.
Кстати комманды лучше всего запускать в Главном меню, а то бот будет немного тупить.
Так же я часто буду бота перезапускать для доработок и новых фишек. А с каждым перезапуском надо обязательно вводить ком\
манду : /start. Ну вы меня услышали🙃
И для тех кто это читает, "секретная" комманда: /top''')
        bot.register_next_step_handler(message, information)
    elif message.text == 'Обратная связь 👨🏻‍💻':
        bc_button = types.InlineKeyboardMarkup()
        bc_button.add(types.InlineKeyboardButton('AuF', url='https://t.me/AuF22'))
        bot.send_message(message.chat.id, 'Ваши идеи, мысли, поправки проводок, недостающие проводки и просто по другим причинам мож\
ете обратится к разработчику нажав кнопку ниже 🔽', reply_markup=bc_button)
        bot.register_next_step_handler(message, information)

    elif message.text == b:
        st(message)


    elif message.text == b:
        st(message)

#блок Термины
def termins(message):

    if message.text == b:
        st(message)
    else:
        termin(message)
        bot.register_next_step_handler(message, termins)

def reclaim(message):
    id = message.chat.id
    rec(message)
    if id == my:
        adm_st(message)
    else:
        adm_2(message)

def add_wiring(message):
    id_u = message.chat.id
    if message.text == b:
        if id_u == my:
            adm_st(message)
        else:
            adm_2(message)
    else:
        add_wir(message)
        bot.register_next_step_handler(message, add_wiring)



bot.polling(none_stop=True, interval=0 )
