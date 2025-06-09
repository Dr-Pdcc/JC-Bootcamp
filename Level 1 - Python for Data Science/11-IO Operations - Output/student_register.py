# Prompt the user to enter the number of students to be registered
no_students =int(input("Enter the number of students to register:"))

# Create a new file called reg_form.txt in write mode
with open('reg_form.txt', 'w') as file:
    # Iterate over the number of students, requesting input for the student ID
    for i in range (no_students):
        student_ID = input(f"Enter student ID for student {i + 1}:")
        # Write a new line in the reg_form.txt file, formatted for signatures
        file.write(f"Student ID:  {student_ID} \t{'_ ' * 20} \n")