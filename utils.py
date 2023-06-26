import json
#Here we obtain the data from de json in a dict shape
def get_products():
    with open('jsonfiles\products.json') as f:
        data = json.load(f)
    return data

#Here we create a function to count all the products in the input
def lower_to_upper(input):
    upper_list = (map(lambda x: x.upper(), input))
    return list(upper_list)


def count_product(product, shopp_car):
    z0 = 0
    for i in range (len(shopp_car)):    
        if product == shopp_car[i]:
            z0 = z0 + 1 
    return z0
