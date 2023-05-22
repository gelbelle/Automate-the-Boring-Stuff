import random
import time
import copy

WIDTH = 60
HEIGHT = 20

# Create a list of list for the cells
next_cells = []

for x in range(WIDTH):
    column = []  # Create a new column
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            column.append("#")  # Add a living cell
        else:
            column.append(" ")  # Add a dead cell
    next_cells.append(column)  # next_cells is a list of column lists

while True:  # Main program loop
    print("\n\n\n\n\n\n")  # Separate each step with newlines
    current_cells = copy.deepcopy(next_cells)
    # Print current_cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end="")  # Print the # or space
        print()  # Print a newline at the end of the row

    # Calculate the next step's cells based on current step's cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get neighbouring coordinates
            # "% WIDTH" ensures left is always between 0 and width - 1
            left = (x - 1) % WIDTH
            right = (x+1) % WIDTH

            above = (y-1) % HEIGHT
            below = (y+1) % HEIGHT

            # Count number of living neighbours
            num_neighbours = 0

            if current_cells[left][above] == "#":
                num_neighbours += 1  # Top left neighbour alive
            if current_cells[x][above] == "#":
                num_neighbours += 1  # Top neighbour alive
            if current_cells[right][above] == "#":
                num_neighbours += 1  # Top right neighbour alive
            if current_cells[right][y] == "#":
                num_neighbours += 1  # Right neighbour is alive
            if current_cells[left][y] == "#":
                num_neighbours += 1  # Left neighbour alive
            if current_cells[left][below] == "#":
                num_neighbours += 1  # Bottom left neighbour alive
            if current_cells[x][below] == "#":
                num_neighbours += 1  # Bottom neighbour alive
            if current_cells[right][below] == "#":
                num_neighbours += 1  # Bottom right neighbour alive

            # Set cell based on Conway's Game of Life Rules
            if current_cells[x][y] == "#" and (num_neighbours == 2 or num_neighbours == 3):
                next_cells[x][y] = "#"
            elif current_cells[x][y] == " " and num_neighbours == 3:
                next_cells[x][y] = "#"
            else:
                next_cells[x][y] = " "
    time.sleep(1)
