import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from database import Database

class TestRegression(unittest.TestCase):

    def setUp(self):
        self.db = Database("test.db")

        self.db.execute("""
        CREATE TABLE IF NOT EXISTS product(
            pid INTEGER PRIMARY KEY,
            Category TEXT,
            Supplier TEXT,
            name TEXT,
            price REAL,
            qty INTEGER,
            status TEXT
        )
        """)

    def tearDown(self):
        # ✅ clean database after each test
        self.db.execute("DELETE FROM product")

    # ✅ TEST 1
    def test_qty_not_low_stock(self):
        self.db.execute(
            "INSERT INTO product(Category,Supplier,name,price,qty,status) VALUES(?,?,?,?,?,?)",
            ("Cat", "Sup", "RegressionItem", 10, 25, "Active")
        )

        threshold = 5

        low_stock = self.db.fetch(
            "SELECT * FROM product WHERE qty <= ?",
            (threshold,)
        )

        names = [row[3] for row in low_stock]

        self.assertNotIn("RegressionItem", names)

    # ✅ TEST 2
    def test_qty_is_low_stock(self):
        self.db.execute(
            "INSERT INTO product(Category,Supplier,name,price,qty,status) VALUES(?,?,?,?,?,?)",
            ("Cat", "Sup", "LowStockItem", 10, 3, "Active")
        )

        threshold = 5

        low_stock = self.db.fetch(
            "SELECT * FROM product WHERE qty <= ?",
            (threshold,)
        )

        names = [row[3] for row in low_stock]

        self.assertIn("LowStockItem", names)


if __name__ == "__main__":
    unittest.main()