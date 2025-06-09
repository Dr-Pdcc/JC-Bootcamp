# Initialise variables
total = 0
count = 0

# Start the while loop
while True:
    # Prompt the user to enter a number (including instructions to exit the loop) 
    num = int(input("Enter a number (enter -1 to stop):"))
    # Check if number is -1
    if num == -1:
        break #Exit the loop

    # Add the number to the total and increment the count
    total += num
    count += 1

# Calculate the average value of the numbers entered
average = total / count
print(f"The average value is:{average}")