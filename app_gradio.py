import gradio as gr
from checkout import Checkout
from utils import get_products, count_product
from pricing_rules import PricingRules

result_list = []  # This global var is for save the results

def calcula_suma(gift_cards, summer_tshirts, summer_pants):
    global result_list  # Acces to the goblal var

    # Here we define the lists using the inputs from the ui
    gift_cards_list = ["VOUCHER"] * gift_cards
    summer_tshirts_list = ["TSHIRT"] * summer_tshirts
    summer_pants_list = ["PANTS"] * summer_pants

    # Add all the list to make the item list
    result_list = gift_cards_list + summer_tshirts_list + summer_pants_list

    # Creating the objects, using the pricing_rules in the checkout constructor to calculate the total cost 
    pricing_rules = PricingRules()
    checkout = Checkout(pricing_rules)

    # Generating a inventory from the json.
    inventory = get_products()

    # Scanning the list item one item at a time
    for each in result_list:
        checkout.scan(each, inventory)

    # Printing the list of items and the total amount.
    result_output = (f"""  
      
    The price for: {count_product('VOUCHER', result_list)} Gift Cards,  {count_product('TSHIRT', result_list)} Summer T-Shirts and  {count_product('PANTS', result_list)} Summer Pants
    
    is: {checkout.total_without_offers(inventory)} dollars without the offers, with offers is: {checkout.calculate_total(inventory)} dollars
    
    """)
    
    return result_output

inputs=[
    gr.components.Slider(minimum=0, maximum=50, step=1, label="Gift cards"),
    gr.components.Slider(minimum=0, maximum=50, step=1, label="Summer t-shirts"),
    gr.components.Slider(minimum=0, maximum=50, step=1, label="Summer pants"),
]
output_component = gr.components.Label(label="El precio es:")

def run():
    # This is very important, gradio works with one fn (logic), inputs and outputs, you need to move all the logic of the program to the function in fn
    iface = gr.Interface(fn=calcula_suma, inputs=inputs, outputs=output_component)
    iface.launch()  # Launch the ui

if __name__ == "__main__":
    run()