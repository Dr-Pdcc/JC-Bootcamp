# Example 1: Static declaration of a 2D list
grayscale_image = [[236, 189, 189, 0], 
                   [236, 80, 189, 189],
                   [236, 0, 189, 80],
                   [236, 189, 189,80]]

print(f"Example 1: {grayscale_image}")
# Example 2: Ddynamic declaration of a 2D list

# Initialise variables for the specific size of the grid.
# In this case we have a 3 by 2 grid
number_of_rows = 3
number_of_columns = 2

# Create the None value twice in a list for the columns, 
# then employ a loop to do it three times for the number of rows. 
empty_grid = [[None] * number_of_columns for _ in range(number_of_rows)]
print(f"Example 2_a: {empty_grid}")

#This is the same list using a for loop instead of list comprehension
empty_grid_2 = []
for n in range(number_of_rows):
    column = [None] * number_of_columns
    empty_grid_2.append(column)
print(f"Example 2_b: {empty_grid_2}")

# To loop through grids, we need to make use of nested loops
student_scores = [ [72, 85, 87, 90, 69],
                   [80, 87, 65, 89, 85],
                   [96, 91, 70, 78, 97],
                   [90, 93, 91, 90, 94] ]

# Use a loop to print all elements of the two dimensional array
print("Example 3:")
row_index = 0
for row in student_scores: # outer loop or rows
    print(f"Term {row_index + 1}: ") # row index for the term number
    row_index +=1
    for col in row: # inner loop for columns
        print(col, end = "% ")
    print()

# Ragged 2D lists - Non-rectangular lists
ragged_list = [ [1, 2, 3],
                [4, 4],
                [6],
                [7, 8, 9, 10] ]
# To iterate thorugh a ragged list we would need to:
# determine the lenght of the current list in the loop
# before running the loop, and for each iteration of the nested loop, 
# update the length to be the length of the current row. 

rows = len(ragged_list)
for row in range(rows):
    cols = len(ragged_list[row]) # the number of cols depends on eachs row's length
    print("Row", row, "has", cols, "columns: ", end="")
    for col in range(cols):
        print(ragged_list[row][col], " ", end="")
    print()
