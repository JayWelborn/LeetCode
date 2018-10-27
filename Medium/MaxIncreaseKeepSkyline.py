class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rmax = [max(row) for row in grid]
        cmax = [max(col) for col in zip(*grid)]
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(rmax[i], cmax[j]) - grid[i][j]
        return ret
