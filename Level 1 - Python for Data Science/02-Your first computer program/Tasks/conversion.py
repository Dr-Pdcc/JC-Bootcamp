'''
Pseudocode:
----------
define variable num1 as 99.23
define variable num2 as 23
define variable num3 as 150
define variable string1 as "100"

convert variable num1 to integer using int()
convert variable num2 to float using float()
convert variable num3 to string using str()
convert variabe string1 to integer using int()

print num1 and the converted num1
print converted num1
print num2 and the converted num2
print num3 and the converted num3
print string1 and the converted string1
'''
#Definining the variables as described in the pseudocode:
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

#Converting the variables by casting them to the desired variable type:
conv_num1 = int(num1)
conv_num2 = float(num2)
conv_num3 = str(num3)
conv_string1 = int(string1)

#Printing the original variable and the converted variable:
print("Original num1:", num1)
print("Converted num1:", conv_num1)

print("Original num2:", num2)
print("Converted num2:", conv_num2)

print("Original num3:", num3)
print("Converted num3:", conv_num3)

print("Original string1:", string1)
print("Converted string1:", conv_string1)