import sqlite3

class Database:
    def __init__(self, db_name="ims.db"):
        self.db_name = db_name

    def connect(self):
        return sqlite3.connect(self.db_name)

    def execute(self, query, params=()):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            conn.commit()

    def fetch(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        data = cur.fetchall()
        conn.close()
        return data
