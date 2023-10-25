import sqlite3


class Database():
    def __init__(self, table_name):
        self.conn = sqlite3.connect('attendance.db')
        self.cursor = self.conn.cursor()
        self.table_name = table_name

    def create_table(self):
        query = f"CREATE TABLE {self.table_name}(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            password INTEGER
            )"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self):
        query = f"INSERT INTO {self.table_name} (password) VALUES (?)"
        self.cursor.execute(query)
        self.conn.commit()
