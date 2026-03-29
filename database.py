class Database:
    def connect(self):
        import sqlite3
        return sqlite3.connect("ims.db")

    def execute(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        conn.commit()
        conn.close()

    def fetch(self, query, params=()):
        conn = self.connect()
        cur = conn.cursor()
        cur.execute(query, params)
        data = cur.fetchall()
        conn.close()
        return data