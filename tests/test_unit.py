import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from billing import BillingUI

class TestBilling(unittest.TestCase):
    from billing import BillingUI

    def setUp(self):
        self.app = type('', (), {})()
        self.app.cart_list = []

        # ✅ bind methods properly
        self.app.calculate_total = BillingUI.calculate_total.__get__(self.app)
        self.app.bill_update = BillingUI.bill_update.__get__(self.app)

        self.app.DISCOUNT_RATE = 5

        # mock labels
        self.app.lbl_amnt = type('', (), {"config": lambda *a, **k: None})()
        self.app.lbl_net_pay = type('', (), {"config": lambda *a, **k: None})()
        self.app.cartTitle = type('', (), {"config": lambda *a, **k: None})()

    # ✅ TEST 1
    def test_calculate_total(self):
        self.app.cart_list = [
            ["1", "Item1", "10", "2"],
            ["2", "Item2", "5", "3"]
        ]
        total = self.app.calculate_total()
        self.assertEqual(total, 35)

    # ✅ TEST 2
    def test_bill_update(self):
        self.app.cart_list = [
            ["1", "Item1", "10", "2"],
            ["2", "Item2", "5", "3"]
        ]

        self.app.bill_update()

        self.assertEqual(self.app.bill_amnt, 35)
        self.assertEqual(self.app.discount, 1.75)
        self.assertEqual(self.app.net_pay, 33.25)

    # ✅ TEST 3
    def test_empty_cart(self):
        self.app.cart_list = []
        total = self.app.calculate_total()
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()