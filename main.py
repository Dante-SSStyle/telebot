import telebot
import sqlite3
from Functions.functions import remove_p, list_p, sum_p
from telebot import types
from Functions.sql import create_table

with open('token.txt', 'r') as key:
    token = key.readline().strip()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = types.KeyboardButton('Добавить')
    item2 = types.KeyboardButton('Удалить')
    item3 = types.KeyboardButton('Список')
    item4 = types.KeyboardButton('Сумма')

    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)

    create_table()

    bot.send_message(message.chat.id, 'Вперде!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def handle_text(message):

    if message.text.strip() == 'Добавить':

            def go(message):

                def name(message):
                    n = message.text

                    def cat(message):
                        c = message.text

                        def price(message):
                            p = message.text
                            try:
                                connection = sqlite3.connect('Fat_o_bot.db')
                                cursor = connection.cursor()
                                cursor.execute(f"""INSERT INTO FatTable(name, category, price)
                                     VALUES('{n}', '{c}', {p});""")
                                connection.commit()
                            except sqlite3.Error as error:
                                bot.send_message(message.chat.id, 'Ошибка базы данных', error)
                            finally:
                                cursor.close()
                            bot.send_message(message.chat.id, 'Добавлено!')

                        msg3 = bot.send_message(message.chat.id, 'Введите цену!')
                        bot.register_next_step_handler(msg3, price)

                    msg2 = bot.send_message(message.chat.id, 'Введите категорию!')
                    bot.register_next_step_handler(msg2, cat)

                msg1 = bot.send_message(message.chat.id, 'Введите название!')
                bot.register_next_step_handler(msg1, name)

            msg = bot.send_message(message.chat.id, 'Отправьте что-угодно для продолжения...')
            bot.register_next_step_handler(msg, go)

    elif message.text.strip() == 'Удалить':
        msg1 = bot.send_message(message.chat.id, 'Введите id для удаления')
        bot.register_next_step_handler(msg1, remove_p)

    elif message.text.strip() == 'Список':
        list_p(message)

    elif message.text.strip() == 'Сумма':
        sum_p(message)

    else:
        bot.send_message(message.chat.id, 'Ты втираешь мне какую-то дичь...')







bot.infinity_polling()
