import json
#Here we obtain the data from de json in a dict shape
def get_products():
    file = open("prueba_tecnica_nextail\products.json")
    data = json.load(file)
    return data

#Here we create a function to count all the products in the input

def count_product(product, shopp_car):
    z0 = 0
    for i in range (len(shopp_car)):    
        if product == shopp_car[i]:
            z0 = z0 + 1 
    return z0

