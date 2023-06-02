import unittest
from checkout import Checkout
from utils import get_products, count_product
from pricing_rules import PricingRules

class TestCheckout(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = PricingRules()
        self.checkout = Checkout(self.pricing_rules)
        self.inventory = get_products()
        self.items_list = ('VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'PANTS', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT')

    def test_scan_valid_item(self):
        try:
            self.checkout.scan('VOUCHER', self.inventory)
            self.assertEqual(self.checkout.get_cart(), ['VOUCHER'])
            print("test_scan_valid_item OK")
        except AssertionError:
            print("test_scan_valid_item FAIL")

    def test_scan_invalid_item(self):
        try:
            self.checkout.scan('INVALID', self.inventory)
            self.assertEqual(self.checkout.get_cart(), [])
            print("test_scan_invalid_item OK")
        except AssertionError:
            print("test_scan_invalid_item FAIL")

    def test_get_cart(self):
        try:
            for item in self.items_list:
                self.checkout.scan(item, self.inventory)
            self.assertEqual(self.checkout.get_cart(), ['VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'PANTS', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT'])
            print("test_get_cart OK")
        except AssertionError:
            print("test_get_cart FAIL")

    def test_total_without_offers(self):
        try:
            for item in self.items_list:
                self.checkout.scan(item, self.inventory)
            total_without_offers = self.checkout.total_without_offers(self.checkout.get_cart(), self.inventory)
            self.assertEqual(total_without_offers, 257.5)
            print("test_total_without_offers OK")
        except AssertionError:
            print("test_total_without_offers FAIL")

    def test_calculate_total(self):
        try:
            for item in self.items_list:
                self.checkout.scan(item, self.inventory)
            total = self.checkout.calculate_total(self.checkout.get_cart(), self.inventory)
            self.assertEqual(total, 232.5)
            print("test_calculate_total OK")
        except AssertionError:
            print("test_calculate_total FAIL")

if __name__ == '__main__':
    unittest.main()

