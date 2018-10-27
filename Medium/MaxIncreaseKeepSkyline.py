class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_maxes = [0] * len(grid)
        col_maxes = [0] * len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > row_maxes[i]:
                    row_maxes[i] = grid[i][j]
                
                if grid[i][j] > col_maxes[j]:
                    col_maxes[j] = grid[i][j]
        
        ret_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < row_maxes[i] and grid[i][j] < col_maxes[j]:
                    ret_sum += min(row_maxes[i], col_maxes[j]) - grid[i][j]
        return ret_sum
