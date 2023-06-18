
# In this file I created the offers like methods in the class
# Inside every method is the condition, so you cant apply the special price to other object or without the condition
# First of all import the function count_product
from utils import count_product

class PricingRules:
    
    # Count the product and with two / / the number is always the lower int, so if you buy one 1 // 2 is 0    
    def twoforone (self, item, product,shop_car, total):
        product_count = count_product(product, shop_car)
        discount_amount = (product_count // 2) * item[product]["price"]
        
        
        return total - discount_amount
    
        
    def three_nineteen (self, product, shop_car, total):
        
        product_count = count_product(product, shop_car)
        if product_count >= 3:
            discount_amount = product_count
        
        else:
            discount_amount = 0    
             
        
        return total - discount_amount
        
                