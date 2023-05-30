import json

def get_products():
    file = open("prueba_tecnica_nextail\products.json")
    data = json.load(file)
    return data

products = get_products()

print(products.keys())


# def price_per_product():
    
