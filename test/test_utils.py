import unittest
from utils import count_product

class TestUtils(unittest.TestCase):
    def test_count_product(self):

        items_list = ('VOUCHER', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'VOUCHER', 'TSHIRT', 'PANTS', 'TSHIRT', 'VOUCHER', 'VOUCHER', 'PANTS', 'TSHIRT')
        voucher_count = count_product("VOUCHER", items_list)
        tshirt_count = count_product("TSHIRT", items_list)
        pants_count = count_product("PANTS", items_list)
        self.assertEqual(voucher_count, 7)
        self.assertEqual(tshirt_count, 10)
        self.assertEqual(pants_count, 3)

if __name__ == '__main__':
    unittest.main()

