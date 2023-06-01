
# In this file I created the offers like methods in the class
# Inside every method is the condition, so you cant apply the special price to other object or without the condition
# First of all import the function count_product
from utils import count_product

class PricingRules:
    def __init__(self):
        self.discount_strategies = {}
    
    # Count the product and with two / / the number is always the lower int, so if you buy one 1 // 2 is 0    
    def twoforone (self, item, shop_car, total):
        voucher_count = count_product("VOUCHER", shop_car)
        discount_amount = (voucher_count // 2) * item["VOUCHER"]["price"]
        
        
        return total - discount_amount
    
        
    def three_nineteen (self,  shop_car, total):
        
        tshirt_count = count_product("TSHIRT", shop_car)
        if tshirt_count >= 3:
            discount_amount = tshirt_count
        
        else:
            discount_amount = 0    
             
        
        return total - discount_amount
        
                