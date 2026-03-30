import sqlite3

class Database:
    def __init__(self, db_name="ims.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute(self, query, params=()):
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()
        finally:
            conn.close()

    def fetch(self, query, params=()):
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(query, params)
            return cur.fetchall()
        finally:
            conn.close()
