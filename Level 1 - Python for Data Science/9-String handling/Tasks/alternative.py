my_string = "The Data Science course is great"

alternative_letters = " " # Empty string to store converted letters
index = 0 # Counter

# Iterate over each letter
for letter in my_string:
    # Even index is uppercase 
    if index % 2 == 0:
        alternative_letters += letter.upper()
    # Odd index is lowercase
    else:
        alternative_letters += letter.lower()
    index += 1
print(alternative_letters)

words = my_string.split() # Split the input string into words
alternative_words = [] # Empty list to store the converted words
index = 0 # Counter

# Iterate over the words
for word in words:
    # Even index is lowercase
    if index % 2 == 0:
        alternative_words.append(word.lower())
    # Odd index is uppercase
    else:
        alternative_words.append(word.upper())
    index += 1 # Increment the index for each word

# Join the words back into a single string
print (" ".join(alternative_words))
