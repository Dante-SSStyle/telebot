import telebot
import sqlite3


with open('token.txt', 'r') as key:
    token = key.readline().strip()

bot = telebot.TeleBot(token)


def remove_p(message):
    die = message.text
    die = int(die)
    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        print(die)
        cursor.execute(f"""DELETE FROM FatTable WHERE id = {die};""")
        connection.commit()
    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка базы данных', error)
    finally:
        cursor.close()
    bot.send_message(message.chat.id, 'Удалено!')


def list_p(message):
    sps = ''
    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM FatTable;')
        sss = 'Список пуст!'
        for i in cursor:
            sps += (str(i) + '\n')
            sss = (f'id        Дата               Имя          Категория и Цена' + '\n' + sps)
        bot.send_message(message.chat.id, sss)

    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка базы данных', error)
    finally:
        cursor.close()


def sum_p(message):
    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        cursor.execute(f"""SELECT sum(price) FROM FatTable""")
        bot.send_message(message.chat.id, cursor)
    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка базы данных', error)
    finally:
        cursor.close()