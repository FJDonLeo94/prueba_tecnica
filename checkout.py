
class Checkout:
    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.items = []

    # The scan method have a condition, if the product from the input isn´t in the inventory this cant scan it
    
    def scan(self, product, inventory):
        if product in inventory:
            self.items.append(product)
        return self.items
    
    # This is only to get the complete list without arguments and use it in the code
    def get_car (self):
        return self.items
    
    def calculate_total(self, shopp_car, inventory):
        total = 0.0
        
        # Calculate the total without offers, the, in case that are offers we can just substract it from the total
        for i in range (len(shopp_car)):    
            if shopp_car[i] in inventory:
                total += inventory[shopp_car[i]]["price"]
                
        # Apply the special price rules to substract the offer from the total
        total = self.pricing_rules.twoforone(inventory, self.get_car(), total)
        total = self.pricing_rules.three_nineteen(self.get_car(), total)
        return total