# Import functions and class

from checkout import Checkout
from utils import get_products, count_product, lower_to_upper
from pricing_rules import PricingRules

z_pants = 0
z_tshirt = 0
z_voucher = 0


# Using one list to work with and transforming the lowercase letters to uppercase to match the inventory list.
item_input = (
    "VOUCHER",
    "TSHIRT",
    "voucher",
    "VOUCHER",
    "PANTS",
    "TSHIRT",
    "TSHIRT",
    "TSHIRT",
    "TSHIRT",
    "TSHIRT",
    "VOUCHER",
    "TSHIRT",
    "VOUCHER",
    "TSHIRT",
    "PANTS",
    "TSHIRT",
    "VOUCHER",
    "VOUCHER",
    "PANTS",
    "TSHIRT",
)
items_list = lower_to_upper(item_input)


# Creating the objects, using the pricing_rules in the checkout constructor to calculate the total cost
pricing_rules = PricingRules()
checkout = Checkout(pricing_rules)

# Generating a inventory from the json.
inventory = get_products()


# Scanning the list item one item at a time
for each in items_list:
    checkout.scan(each, inventory)
    if each == 'VOUCHER':
        z_voucher += 1
    elif each == 'TSHIRT':
        z_tshirt += 1
    elif each == 'PANTS':
        z_pants += 1
        


# Printing the list of items and the total amount.
print(
    f"""  
      
    The price for:
      
    - {z_voucher} Gift Cards, 
    - {z_tshirt} Summer T-Shirts and 
    - {z_pants} Summer Pants
    
    is: {checkout.total_without_offers(inventory)} dollars without the offers, with offers is: {checkout.calculate_total(inventory)} dollars
    
    """
)
 