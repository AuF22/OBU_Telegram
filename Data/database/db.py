import sqlite3 as sq
from aiogram import Dispatcher
from Data.config import admins_id


class DataBase:
    def __init__(self):
        self.db = sq.connect('user_id.db')
        self.cursor = self.db.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS user(user_id TEXT PRIMARY KEY, name TEXT)""")
        self.db.commit()

    async def create_profile(self, user_id: str, name: str) -> None or str:
        user = self.cursor.execute("""SELECT 1 FROM user WHERE user_id == {key}""".format(key=user_id)).fetchone()
        if not user:
            self.cursor.execute("""INSERT INTO user VALUES(?,?)""", (user_id, name))
            self.db.commit()
            return 'Новый пользователь'
        else:
            return None
