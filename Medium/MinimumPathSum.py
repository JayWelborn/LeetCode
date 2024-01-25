class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        for row in range(height):
            for col in range(width):
                if row or col:
                    if row == 0:
                        grid[row][col] = grid[row][col] + grid[row][col - 1]
                    elif col == 0:
                        grid[row][col] = grid[row][col] + grid[row - 1][col]
                    else:
                        grid[row][col] = min(grid[row - 1][col], grid[row][col - 1]) + grid[row][col]

        return grid[-1][-1]
