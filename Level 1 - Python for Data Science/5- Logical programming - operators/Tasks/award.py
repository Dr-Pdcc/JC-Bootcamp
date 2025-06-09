# Triathlon Award
# This script determines the award triathlon participants should receive based on their completion time.

# Prompt the user to enter the time recorded for the swimming, cycling, and running stages of the triathlon (in minutes)
swimming_time = int(input("Enter your swimming time in minutes:"))
cycling_time = int(input("Enter your cycling time in minutes:"))
running_time = int(input("Enter your running time in minutes:"))

# Calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time
# Print the total completion time
print(f"Total time taken for the thriatlon:{total_time} minutes")

# Determine the award based on the total completion time
if total_time <= 100:
    # Award for participants completing within 100 minutes or less
    print("Award: Provincial colours")
elif total_time <= 105:
    # Award for participants completing between 101 and 105 minutes
    print("Award: Provincial half colours")
elif total_time <= 110:
    # Award for participants completing between 106 and 110 minutes
    print("Award: Provincial scroll")
else:
    # No award for participants exceeding 110 minutes
    print("No award")