class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height = len(grid)
        width = len(grid[0])

        path_sums = [[0 for i in range(width)] for i in range(height)]

        path_sums[0][0] = grid[0][0]

        for col in range(1, width):
            path_sums[0][col] = grid[0][col] + path_sums[0][col - 1]
        for row in range(1, height):
            path_sums[row][0] = grid[row][0] + path_sums[row - 1][0]

        for col in range(1, width):
            for row in range(1, height):
                path_sums[row][col] = min(path_sums[row-1][col], path_sums[row][col-1]) + grid[row][col]

        return path_sums[height-1][width-1]
