import unittest
from pricing_rules import PricingRules

class TestPricingRules(unittest.TestCase):
    def setUp(self):
        self.pricing_rules = PricingRules()
        self.inventory = {
            "VOUCHER": {
                "name": "Gift Card",
                "price": 5.00
            },
            "TSHIRT": {
                "name": "Summer T-Shirt",
                "price": 20.00
            },
            "PANTS": {
                "name": "Summer Pants",
                "price": 7.50
            }
        }

    def test_twoforone_discount(self):
        try:
            shop_car = ['VOUCHER', 'VOUCHER', 'VOUCHER']
            total = 15.00  # Total without discount: 15.00
            total_with_discount = self.pricing_rules.twoforone(self.inventory, shop_car, total)
            self.assertEqual(total_with_discount, 10.00)  # Total with 2-for-1 discount: 10.00
            print("test_twoforone OK")
        except AssertionError:
            print("test_stwoforone FAIL")

    def test_three_nineteen_discount(self):
        try:
            shop_car = ['TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT']
            total = 80.00  # Total without discount: 80.00
            total_with_discount = self.pricing_rules.three_nineteen(shop_car, total)
            self.assertEqual(total_with_discount, 76)  # Total with 4-for-19 discount: 76.00
            print("test_three_nineteen_discount OK")
        except AssertionError:
            print("test_three_nineteen_discount FAIL")
            
    def test_no_discount(self):
        try:
            shop_car = ['VOUCHER', 'TSHIRT', 'PANTS']
            total = 32.50  # Total without discount: 32.50
            total_with_discount = self.pricing_rules.twoforone(self.inventory, shop_car, total)
            total_with_discount = self.pricing_rules.three_nineteen(shop_car, total_with_discount)
            self.assertEqual(total_with_discount, 32.50)  # No discount applied, total remains the same
            print("test_no_discount OK")
        except AssertionError:
            print("test_no_discount FAIL")

if __name__ == '__main__':
    unittest.main()


