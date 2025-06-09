str_manip = input("Enter a sentence:")

length = len(str_manip)
print("Length:", length)

last_letter = str_manip[-1]
modified_str = str_manip.replace(last_letter, '@')
print(f"Modified sentence:{modified_str}")

# Take the last three characters: last_3 = str_manip[-3:]
# Reverse the last 3 characters last_3_reversed = last3[::-1]
last_3_reversed = str_manip[-3:][::-1]
print(f"Last 3 characters reversed:{last_3_reversed}")

New_word = str_manip[:3] + str_manip[-2:]
print(f"New word:{New_word}")