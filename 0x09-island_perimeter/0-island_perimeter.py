#!/usr/bin/python3
"""
grid
"""
def island_perimeter(grid):
    perimeter = 0
    height = len(grid)
    width = len(grid[0])
    
    for row in range(height):
        for col in range(width):
            if grid[row][col] == 1:
                # if the cell is land, add its perimeter
                perimeter += 4
                # check if there is land to the left, and if so subtract 2 from the perimeter
                if col > 0 and grid[row][col-1] == 1:
                    perimeter -= 2
                # check if there is land above, and if so subtract 2 from the perimeter
                if row > 0 and grid[row-1][col] == 1:
                    perimeter -= 2
    return perimeter