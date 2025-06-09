# The objective of this task is to write a program with two
#compilation errors, a runtime error and a logical error. 

# Compilation error 1: missing colon in 'if' statement
age = 18
if age >= 18 # Syntax error: missing colon (this should be 'if age >= 18:')
    print("You can enter the club")

# Compilation error 2: using an assigment '=' instead of a comparison
user_number = input("Enter a number: ")
if user_number = 25: # Syntax error: this should be '==' instead of '='
    print(f"You entered number{user_number}")

# Runtime error: trying to concatenate an integer and a string
age = int(input("Enter your age: "))
print("In 5 years you will be" + (age + 5) + "years old")
# TypeError: this should use str(age + 5)

# Logical error: incorrect area calculation for a rectangle
length = 7
width = 5
rectangle_area = length + width # Logical error: this should be 'length' * 'width'

print(f"Rectangle area: {rectangle_area}") # Incorrect output: 12 instead of 35