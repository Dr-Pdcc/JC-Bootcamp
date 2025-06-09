#===Validation check on user full name===
# This script validates the user's input for a full name based on length criteria.

# Prompt the user to enter their full name
full_name = input("Enter your full name:")

# Check if the user didn't enter anything (empty input)
if len(full_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
# Check if the input is too short to be a full name
elif len(full_name) < 4:
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")
# Check if the input is excessively long to ensure only the full name was provided
elif len(full_name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")
# If the input passes all validations, thank the user
else:
    print("Thank you for entering your name.")