import sqlite3


def create_table():
    try:
        connection = sqlite3.connect('Fat_o_bot.db')
        cursor = connection.cursor()
        sqlite_create_table = """CREATE TABLE IF NOT EXISTS FatTable(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT DEFAULT CURRENT_DATE,
            name TEXT, 
            category TEXT,
            price REAL);     
        """
        cursor.execute(sqlite_create_table)
        connection.commit()

    except sqlite3.Error as error:
        bot.send_message(message.chat.id, 'Ошибка SQLite', error)

    finally:
        cursor.close()