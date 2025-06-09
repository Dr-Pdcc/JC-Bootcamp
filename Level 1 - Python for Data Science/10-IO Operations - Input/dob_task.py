# Open the 'DOB.txt' file in read and write mode
with open('DOB.txt', 'r+') as file:
    # Create empty lists to store names and birthdates
    names = []
    birthdates = []
    #Iterate over each line in the file
    for line in file:
        #Split each line into words based on whitespace
        words = line.split()
        # Join the first two words to form the full name
        name = " ".join(words[:2])
        # Join the remaning words to for the date of birth
        birthdate = " ".join(words[2:])
        # Append the extracted name and birthdate to the previously created empty lists
        names.append(name)
        birthdates.append(birthdate)

# Print the heading for the list of names in bold format using ANSI escape code
# See reference: https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
print("\033[1mName\033[0m") # \033[1m: Start bold, \033[0m: End bold

# Iterate through the list of names and print each one
for name in names:
    print(name)

# Print a separator and the heading for birthdates
print("\n\033[1mBirthdate\033[0m")

# Iterate through the list of birthdates and print each one
for birthdate in birthdates:
    print(birthdate)
