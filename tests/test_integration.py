import unittest
from database import Database
import os

class TestIntegration(unittest.TestCase):

    def test_add_and_fetch_product(self):
        db = Database()

        db.execute(
            "INSERT INTO product(Category,Supplier,name,price,qty,status) VALUES(?,?,?,?,?,?)",
            ("TestCat", "TestSup", "TestProduct", "10", "5", "Active")
        )

        result = db.fetch(
            "SELECT * FROM product WHERE name=?",
            ("TestProduct",)
        )

        self.assertTrue(len(result) > 0)

    def test_update_quantity(self):
        db = Database()

        db.execute(
            "INSERT INTO product(Category,Supplier,name,price,qty,status) VALUES(?,?,?,?,?,?)",
            ("Cat", "Sup", "TestItem", "10", "10", "Active")
        )

        product = db.fetch("SELECT * FROM product WHERE name=?", ("TestItem",))
        pid = product[0][0]

        db.execute(
            "UPDATE product SET qty=? WHERE pid=?",
            (5, pid)
        )

        updated = db.fetch("SELECT qty FROM product WHERE pid=?", (pid,))
        self.assertEqual(int(updated[0][0]), 5)


if __name__ == "__main__":
    unittest.main()