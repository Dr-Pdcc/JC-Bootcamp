# Function to print the grid
def make_grid(grid):
    for row in grid:
        print(" ".join(row))

# Function to count the number of mines adjacent to a given cell 
def count_mines(grid, row, col):
    # List of 8 possible neighbour cell positions (relative to the current cell)
    directions = [(-1, -1), (-1, 0), (-1, 1), # NW, N, NE
                  (0, -1),           (0, 1),  # W, E
                  (1, -1),  (1, 0),  (1, 1)]  # SW, S, SE
    
    count = 0 # Counter for adjacent mines 

    # Iterate through all possible neighbour positions
    for dr, dc in directions:
        r = row + dr  # Calculate the row index of the neighbour cell
        c = col + dc  # Calculate the column index of the neighbour cell
    
        # Check if the new position is within the bounds and contains a mine
        if (0 <= r < len(grid) and 
            0 <= c < len(grid[0]) and 
            grid[r][c] == "#"):
            count += 1 # Increment the mine count
    return count

# Function to generate the Minesweeper grid with numbers replacing empty cells
def minesweeper(grid):
    result = []
    # Iterate through each row
    for row in range (len(grid)):
        new_row = [] # Initialise the output grid

        # Iterate through each column in the row
        for col in range(len(grid[row])):
            if grid[row][col] == "#":
                new_row.append("#") # Keep mines as they are
            else:
                # Replace empty spots ('-') with the count of adjacent mines
                new_row.append(str(count_mines(grid, row, col)))
        result.append(new_row) # Append the processed row to the result grid
    return result

# Function to print the transformed grid in a clean format
def print_grid(grid):
    for row in grid:
        print(" ".join(row))

# Example Input
grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Process the grid and print the result
output_grid = minesweeper(grid)
print("Original grid:")
print_grid(grid)
print("Processed grid:")
print_grid(output_grid) # print(output_grid) would print a nested list structure