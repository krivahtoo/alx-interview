#!/usr/bin/python3
"""
0. Island Perimeter
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in the grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # Land cell
                # Start with 4 sides for the land cell
                perimeter += 4

                # Check for adjacent land cells and subtract shared edges
                if i > 0 and grid[i - 1][j] == 1:  # Up
                    perimeter -= 1
                if i < rows - 1 and grid[i + 1][j] == 1:  # Down
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:  # Left
                    perimeter -= 1
                if j < cols - 1 and grid[i][j + 1] == 1:  # Right
                    perimeter -= 1

    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
