# =====importing libraries===========
'''This is the section where you will import libraries'''
# See reference: https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python
from datetime import datetime

# Function to load users from 'user.txt' file
def load_users():

    users = {}
    with open("user.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password.strip()  # Remove any surrounding spaces/newlines
    return users

# Function to validate dates
def check_date(input_date):

    date_formats = ["%d-%m-%Y", "%d %b %Y", "%d/%m/%Y"]
    for date_format in date_formats:
        try:
            return datetime.strptime(input_date, date_format).strftime("%d %b %Y")
        except ValueError:
            continue
    return None

# Display statistics for admin
def display_statistics():

    # Count total number of users
    with open("user.txt", "r") as file:
        total_users = sum(1 for _ in file)

    # Count total number of tasks
    with open("tasks.txt", "r") as file:
        total_tasks = sum(1 for _ in file)

    print(f"\nTotal number of users: {total_users}")
    print(f"Total number of tasks: {total_tasks}\n")


# ====Login Section====
users = load_users()

while True:
    # Prompt the user to enter their username and password for login
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        break
    print("Invalid username or password. Try again")

# ==== Main Menu Loop ====
while True:
    menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
ds - display statistics (admin only)
e - exit
: ''').lower()  # Ensure input is case-insensitive

    if menu == 'r':
        # Added new condition - now only the admnin can register new users
        if username != 'admin':
            print("Only the 'admin' user is allowed to register new users.")
        else:
            # Register a new user
            new_username = input("Enter a new username: ")
            if new_username in users:
                print("That username already exists. Enter a new username.")
                continue  # Skip the rest of the loop and prompt again

            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm new password: ")

            if new_password == confirm_password:
                with open("user.txt", "a") as file:
                    file.write(f"\n{new_username}, {new_password}")
                users[new_username] = new_password
                print("New user registered successfully.")
            else:
                print("Passwords do not match. Please, try again.")

    elif menu == 'a':
        # Add a new task
        assigned_user = input("Enter the username of the person assigned: ")
        if assigned_user not in users:
            print(f"The user {assigned_user} is not registered."
                  "Enter a registered user.")
            continue  # Stop the task creation and return to the main menu

        task_title = input("Enter the task title: ")
        task_description = input("Enter the task description: ")

        # Check for due date input
        while True:
            due_date_input = input(
                "Enter the due date (e.g., 10 Feb 2025  or 10-02-2025): "
            )
            due_date = check_date(due_date_input)
            if due_date:
                break
            else:
                print(
                    "Invalid date format. Please enter a valid date in"
                    "the format 'DD MMM YYYY' or 'DD-MM-YYYY'."
                )

        assigned_date = datetime.today().strftime("%d %b %Y")

        # Add task to file
        with open("tasks.txt", "a") as file:
            file.write(
                f"\n{assigned_user}, {task_title}, {task_description}, "
                f"{assigned_date}, {due_date}, No"
            )
        print("Task added successfully!")

    elif menu == 'va':
        # View all tasks
        with open("tasks.txt", "r") as file:
            for line in file:
                task_data = line.strip().split(", ")
                print("_" * 70)  # Separator line between tasks
                print(f"Task: \t\t {task_data[1]}")
                print(f"Assigned to: \t {task_data[0]}")
                print(f"Date assigned: \t {task_data[3]}")
                print(f"Due date: \t {task_data[4]}")
                print(f"Task Complete? \t {task_data[5]}")
                print(f"Task description:\n  {task_data[2]}")
                print("_" * 70)  # Separator line between tasks

    elif menu == 'vm':
        # View tasks assigned to the logged-in user
        with open("tasks.txt", "r") as file:
            found = False
            for line in file:
                task_data = line.strip().split(", ")
                if task_data[0] == username:
                    found = True
                    print("_" * 70)  # Separator line between tasks
                    print(f"Task: \t\t {task_data[1]}")
                    print(f"Assigned to: \t {task_data[0]}")
                    print(f"Date assigned: \t {task_data[3]}")
                    print(f"Due date: \t {task_data[4]}")
                    print(f"Task Complete? \t {task_data[5]}")
                    print(f"Task description:\n  {task_data[2]}")
                    print("_" * 70)  # Separator line between tasks
            if not found:
                print("No tasks assigned to you.")

    elif menu == 'ds':
        if username == 'admin':
            # Display user statistics (admnin view only)
            display_statistics()
        else:
            print("Only the 'admin' user can view the statistics.")

    elif menu == 'e':
        print('Goodbye!!!')
        exit()  # Exit the program

    else:
        print("You have entered an invalid input. Please try again")
