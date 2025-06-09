# The objective of this task is to write a program that demonstrate logical errors 

original_price = float(input("Enter the item's original price:"))
discount = float(input("Enter the discount percentage:"))

# Discounted price
# Logical error: this calculation should be 'original_price * (1 - discount / 100)
discounted_price = original_price * discount

# Print the final price
print(f"After applying a {discount}% discount, the final price is: £{discounted_price}")