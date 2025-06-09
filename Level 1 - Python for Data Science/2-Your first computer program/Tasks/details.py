'''
Pseudocode:
----------
ask the user to input their name and store it in variable name
ask the user to input their age and store it in variable age
ask the user to input their house number and store it in variable house_number
ask the user to input their street name and store it in variable street_name
print a single sentence that contains all these stored details
'''
#Declaring varibales as user input, asking for name, age, house number and street name:
name = input("Enter your name:")
age = input("Enter your age:")
house_number = input ("Enter your house number:")
street_name = input ("Enter you street name:")

#Printing a sentence that makes use of the user inputs:
print(f"This is {name}. He is {age} years old and lives at house number {house_number} on {street_name}.")