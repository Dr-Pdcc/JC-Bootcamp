# Define the list of items on the menu
menu = ["espresso", "latte", "mocha", "capuccino", "tea", "sandwich", "brownie"]
# Define a dictionary with stock values for each item on the menu
stock = {
    "espresso": 400, 
    "latte": 370,
    "mocha": 200, 
    "capuccino": 170,
    "tea": 500,
    "sandwich": 50,
    "brownie": 10
    }
# Define a dictionary with price values for each item on the menu
price = {
    "espresso": 2,
    "latte": 2,
    "mocha": 3.50,
    "capuccino": 3.20,
    "tea":1.70,
    "sandwich": 4,
    "brownie": 5.50
    }

# Initialise value of the total stock
total_stock = 0
for item in menu:
    item_value = (stock[item] * price[item]) # Calculate the value for each item
    total_stock += item_value # Add to the total stock worth

'''
This could also be done using list comprehension:

total_stock = sum(stock[item] * price[item] for item in menu)
'''

# Print the calculated value of the total stock worth
print(f"The total stock worth is: {total_stock} pounds")