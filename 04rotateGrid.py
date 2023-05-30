grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


def main():
    """The goal of this program is to take the above grid and rotate it 90 degrees clockwise"""

    for x in range(len(grid[0])):  # Gets the length of the first row
        for y in range(len(grid)):  # Gets the number of rows in the grid
            print(grid[y][x], end="")  # Swaps the x and the y to "rotate" grid
        print("\n")


if __name__ == "__main__":
    main()
