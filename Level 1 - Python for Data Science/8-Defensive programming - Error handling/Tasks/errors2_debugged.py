# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

# Syntax error fixed: 'Lion' is a string, so quotes are required
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Syntax error fixed: added f-string for better formatting
# Logical error: hard to spot but necessary for the sentence to make sense - 'number_of_theet' and 'animal_type' have been reordered
# PS: I am not sure if this should be marked as a Logical error, but it is definitely required for the sentence to make sense
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

# Syntax error fixed: added parentheses to the print() method
print (full_spec)