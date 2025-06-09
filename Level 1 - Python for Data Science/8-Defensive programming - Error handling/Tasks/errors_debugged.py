# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Syntax error fixed: the print() method was missing parentheses
print ("Welcome to the error program")
# Syntax error fixed: the print() method was missing parentheses and unexpected indentation was removed
print ("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax error fixed: unexpected indentation corrected in the following lines (used Shift + Tab)
# Syntax error fixed: used '=' to assign values instead of '=='
# Logical error fixed: a non-numerical string cannot be cast to an integer. Updated 'age_str' to a numeric string
age_str = "24" # Updated variable name from 'age_Str' to 'age_str' for proper snake casing
age = int(age_str) 

# Syntax error fixed: strings can only concatenate to other strings. Used an f-string for better formatting
print(f"I'm {age} years old.") 

# Variables declaring additional years and printing the total years of age
# Syntax error fixed: 'years_from_now' updated to an integer instead of a string
years_from_now = 3
total_years = age + years_from_now

# Syntax error fixed: the print() method was missing parentheses.
# Logical error fixed: used the correct variable 'total_years' instead of the placeholder "answer_years"
# Optional: in my opinion printing this line can be misleading for the user as it is an intermediate calculation. I would wither remove or comment this line. Alternatively, the sentence could be change to something
# more descriptive, such as "In 3 years I will be {total_years} years old"
print (f"The total number of years: {total_years}")

# Variable to calculate the total amount of months from the total amount of years and printing the result
# Syntax error fixed: updated variable name 'total' to 'total_years'
# Logical error fixed: included an additional 6 months to calculate the correct total in 3 years and 6 months
total_months = (total_years * 12) + 6

# Syntax error fixed: the print() method was missing parentheses
# Syntax error fixed: strings can only concatenate to other strings. Used an f-string for better formatting
print (f"In 3 years and 6 months, I'll be {total_months} months old")

