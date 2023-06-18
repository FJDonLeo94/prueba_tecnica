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
    def get_cart (self):
        return self.items
    
    def total_without_offers(self, inventory):
        total_wo_offers = 0
        for i in range (len(self.get_cart())):    
            if self.get_cart()[i] in inventory:
                total_wo_offers += inventory[self.get_cart()[i]]["price"]
        
        return total_wo_offers
    
    def calculate_total(self, inventory):

        # Calculate the total without offers, the, in case that are offers we can just substract it from the total
        total = self.total_without_offers(inventory)
                
        # Apply the special price rules to substract the offer from the total
        total = self.pricing_rules.twoforone(inventory, self.get_cart(), total)
        total = self.pricing_rules.three_nineteen(self.get_cart(), total)
        return total
    