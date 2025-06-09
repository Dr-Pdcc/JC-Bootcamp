#=====importing libraries===========
'''This is the section where you will import libraries'''
# See reference: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from datetime import datetime 

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
def load_users():
    users ={}
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password.strip()
    return users

users = load_users()

while True:
    username = input("Enter username: ")
    password = input("Enter password: ")    

    if username in users and users[username] == password:
        print("Login successful!")
        break
    else:
        print("Invalid username or password. Try again")


while True:
    # Present the menu to the user and 
    # make sure that the user input is converted to lower case.
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        new_username = input("Enter a new username: ")
        if new_username in users:
            print("That username already exists. Please, enter a new username.")
            continue
        new_password = input("Enter a new password: ")
        confirm_password = input("Confirm new password: ")

        if new_password == confirm_password:
            with open("user.txt", "a") as file:
                file.write(f"{new_username}, {new_password}\n")
            users[new_username] = new_password
            print("New user registered successfully.")
        else:
            print("Passwrods do not match. Please, try again.")

    elif menu == 'a':
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''
        assigned_user = input("Enter the username of the person assigned: ")
        task_title = input("Enter the task title: ")
        task_description = input("Enter the task description: ")
        due_date = input("Enter the due date (YYYY-MM-DD): ")
        assigned_date = datetime.today().strftime("%Y-%m-%d")

        with open("tasks.txt", "a") as file:
            file.write(f"{assigned_user}, {task_title}, {task_description}, {assigned_date}, {due_date}, No\n")
        print("Task added successfully!")


    elif menu == 'va':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(", ")
                print(f"Task: \t\t {task_data[1]}")
                print(f"Assigned to: \t {task_data[0]}")
                print(f"Date assigned: \t {datetime.strptime(task_data[3], '%Y-%m-%d').strftime('%d %b %Y')}")
                print(f"Due date: \t {datetime.strptime(task_data[4], '%Y-%m-%d').strftime('%d %b %Y')}")
                print(f"Task Complete? \t {task_data[5]}")
                print(f"Task description:\n  {task_data[2]}")
                print("_" * 70)  # Separator line between tasks


    elif menu == 'vm':
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        with open("tasks.txt", "r") as file:
            found = False
            for line in file:
                task_data = line.strip().split(", ")
                if task_data[0] == username:
                    found = True
                    print(f"Task: \t\t {task_data[1]}")
                    print(f"Assigned to: \t {task_data[0]}")
                    print(f"Date assigned: \t {datetime.strptime(task_data[3], '%Y-%m-%d').strftime('%d %b %Y')}")
                    print(f"Due date: \t {datetime.strptime(task_data[4], '%Y-%m-%d').strftime('%d %b %Y')}")
                    print(f"Task Complete? \t {task_data[5]}")
                    print(f"Task description:\n  {task_data[2]}")
                    print("_" * 70)  # Separator line between tasks
            if not found:
                print("No tasks assigned to you.")
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have entered an invalid input. Please try again")