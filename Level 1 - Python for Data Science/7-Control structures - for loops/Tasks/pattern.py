# Define the total number of rows in the pattern
number_of_rows = 9
# The pattern has 9 rows so the range has to go from 0 to 10 [0:10] since the end index is not included
total_rows = number_of_rows + 1

for i in range (0,total_rows):
        # Takes the upper half of the pattern (including the middle row)
        if i <= (number_of_rows / 2):
              print("*" * i)
        # Takes the lower half of the pattern
        else:
               # The stars decrease as we move further down the lower half
               print ("*" * (total_rows - i))          
        