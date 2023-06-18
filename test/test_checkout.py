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
        
        self.checkout.scan('VOUCHER', self.inventory)
        self.assertEqual(self.checkout.get_cart(), ['VOUCHER'])

    def test_scan_invalid_item(self):

        self.checkout.scan('INVALID', self.inventory)
        self.assertEqual(self.checkout.get_cart(), [])

    def test_get_cart(self):

        for item in self.items_list:
            self.checkout.scan(item, self.inventory)
        self.assertEqual(self.checkout.get_cart(), ['VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'PANTS', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT'])


    def test_total_without_offers(self):

        for item in self.items_list:
            self.checkout.scan(item, self.inventory)
        total_without_offers = self.checkout.total_without_offers(self.inventory)
        self.assertEqual(total_without_offers, 257.5)
    

    def test_calculate_total(self):
        
        for item in self.items_list:
            self.checkout.scan(item, self.inventory)
        total = self.checkout.calculate_total(self.inventory)
        self.assertEqual(total, 232.5)
            

if __name__ == '__main__':
    unittest.main()