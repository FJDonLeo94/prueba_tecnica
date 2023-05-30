class PricingRules:
    def __init__(self):
        self.discount_strategies = {}
        
    def twoforone (self, item, total):
        
        voucher_count = item.count("VOUCHER")
        discount_amount = (voucher_count // 2) * item["VOUCHER"].price
        
        return total - discount_amount
        
    # def bulk (self, item, discount):
        
                