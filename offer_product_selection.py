from utils import get_products

all_products = get_products()
all_products_list = list(all_products.keys())

#Right now, this list is (['VOUCHER', 'TSHIRT', 'PANTS']), if the list json change you should come here and execute  print(all_products_list)



product_2x1 = all_products_list[0]

product_3_19 = all_products_list[1]


