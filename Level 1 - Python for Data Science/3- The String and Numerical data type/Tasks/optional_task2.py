string_fav = input("Enter the name of your favourite restaurant:")
int_fav = int(input("Enter your favourite number:"))

print(f"Your favourite restaurant is: {string_fav} ")
print(f"Your favourite number is: {int_fav}")

#Try to cast string_fav to an integer
int_string_fav = int(string_fav)
'''This causes an error bacuse the name of the restaurant is not numeric.
If the name of the restaurant was numeric, for instance 404, the code would run'''