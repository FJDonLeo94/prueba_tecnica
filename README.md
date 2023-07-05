# Backend Exercise


## How to use

In this program, I used gradio to create a UI that allows to see the backend working in a little demo.

First of all, from the root folder, run ``pip install requirements.txt`` to install gradio, as it is the only external library that is not included in Python.

To run the unit tests, you can execute ``python test_runner.py``. There is one test for every function in the program.
To run a specific test, you can use ``python -m unittest test/file.py``

To run the program, you should execute ``python app_gradio.py``, and if a window doesn´t open, click the ip from the terminal.




## Statement

The first store where we will introduce our software will sell the
following 3 products.

| CODE    | NAME           | PRICE  |
|---------|----------------|--------|
| VOUCHER | Gift Card      | 5.00€  |
| TSHIRT  | Summer T-Shirt | 20.00€ |
| PANTS   | Summer Pants   | 7.50€  |


The different departments have agreed the following discounts:
* A 2-for-1 special on VOUCHER items.
* If you buy 3 or more TSHIRT items, the price per unit should be 19.00€.
* Items can be scanned in any order, and the cashier should return the total amount to be paid.

The interface for the checkout process has the following specifications:
* The Checkout constructor receives a pricing_rules object
* The Checkout object has a scan method that receives one item at a time

Examples:
* Items: VOUCHER, TSHIRT, PANTS - Total: 32.50€
* Items: VOUCHER, TSHIRT, VOUCHER - Total: 25.00€
* Items: TSHIRT, TSHIRT, TSHIRT, VOUCHER, TSHIRT - Total: 81.00€
* Items: VOUCHER, TSHIRT, VOUCHER, VOUCHER, PANTS, TSHIRT, TSHIRT - Total: 74.50€

