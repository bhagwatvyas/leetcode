"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
"""


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        height = len(grid)
        width = len(grid[0])
        # Iterate through the grid
        for i in range(height):
            for j in range(width):
                # Check if the value represents land
                if grid[i][j] == 1:

                    if i == 0:
                        perimeter += 1

                    if j == 0:
                        perimeter += 1

                    if i == height - 1:
                        perimeter += 1

                    if j == width - 1:
                        perimeter += 1

                    if i < height - 1 and grid[i + 1][j] == 0:
                        perimeter += 1

                    if j < width - 1 and grid[i][j + 1] == 0:
                        perimeter += 1

                    if i > 0 and grid[i - 1][j] == 0:
                        perimeter += 1

                    if j > 0 and grid[i][j-1] == 0:
                        perimeter += 1
        return perimeter



sol = Solution()
print(sol.islandPerimeter(
    [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))
