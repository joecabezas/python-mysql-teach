import sys

import mysql.connector

class Main:
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWORD = '123'
    DB_DATABASE = 'macondo'

    DB_TABLE_USER = 'users'

    def __init__(self):
        self.conn = self.create_connection()
        self.create_database()
        self.create_table()

    def create_connection(self):
        return mysql.connector.connect(
            host=self.DB_HOST,
            user=self.DB_USER,
            password=self.DB_PASSWORD,
        )

    def create_database(self):
        cur = self.conn.cursor()
        cur.execute("SHOW DATABASES")

        if self.DB_DATABASE in [item[0] for item in cur]:
            return

        cur.execute(f"CREATE DATABASE {self.DB_DATABASE}")

    def create_table(self):
        cur = self.conn.cursor()
        cur.execute(f"SHOW TABLES FROM {self.DB_DATABASE}")

        if self.DB_TABLE_USER in [item[0] for item in cur]:
            return

        cur.execute(f"CREATE TABLE {self.get_table_name()} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100))")

    def get_table_name(self):
        return f"{self.DB_DATABASE}.{self.DB_TABLE_USER}"

    def add_user(self, name):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO {self.get_table_name()} (name) VALUES(%s)", (name,))

        self.conn.commit()

if __name__ == '__main__':
    main = Main()
    main.add_user(sys.argv[1])
