import telebot
import sqlite3
from telebot import types

token = open('token.txt').readline().strip()
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Добавить')
    item2 = types.KeyboardButton('Удалить')
    item3 = types.KeyboardButton('Список')
    item4 = types.KeyboardButton('Сумма')
    item5 = types.KeyboardButton('Удалить день')

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)

    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        sqlite_create_table = """CREATE TABLE IF NOT EXISTS FatTable(
            дата TEXT DEFAULT CURRENT_TIMESTAMP,
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            категория TEXT,
            название TEXT,
            цена REAL(100000,2));
        """
        cursor.execute(sqlite_create_table)
        connection.commit()

    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка SQLite', error)

    finally:
        cursor.close()

    bot.send_message(message.chat.id, 'Вперде!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text.strip() == 'Добавить':
        msg1 = bot.send_message(message.chat.id, 'Введите название!')
        bot.register_next_step_handler(msg1, name)
    elif message.text.strip() == 'Удалить':
        answer = ('Пока не работает!)')

    elif message.text.strip() == 'Список':
        try:
            connection = sqlite3.connect('Fat_o_bot.db')
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM FatTable;')
            answer = cursor.fetchall()
        except sqlite3.Error as error:
            bot.send_message(message.chat.id, 'Ошибка базы данных', error)
        finally:
            cursor.close()

    elif message.text.strip() == 'Сумма':
        answer = ('Пока не работает!?')
    elif message.text.strip() == 'Удалить день':
        answer = ('Пока не работает!!!!')
    bot.send_message(message.chat.id, answer)

def name(message):
    global n
    n = message.text
    bot.send_message(message.chat.id, n)
    msg2 = bot.send_message(message.chat.id, 'Введите категорию!')
    bot.register_next_step_handler(msg2, cat)

def cat(message):
    global c
    c = message.text
    bot.send_message(message.chat.id, (n+', '+c))
    msg3 = bot.send_message(message.chat.id, 'Введите цену!')
    bot.register_next_step_handler(msg3, price)

def price(message):
    global p
    p = message.text
    bot.send_message(message.chat.id, (n + ', ' + c + ', ' + p))
    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        # cursor.execute(f"""INSERT INTO FatTable(название, категория, цена, дата, id)    Пока не работает
        #     VALUES({n}, {c}, {p});""")  Возможно, нужно пихнуть данные в кортеж и добавить через него
        connection.commit()
    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка базы данных', error)
    finally:
        cursor.close()
    bot.send_message(message.chat.id, 'Добавлено!')






bot.infinity_polling()
