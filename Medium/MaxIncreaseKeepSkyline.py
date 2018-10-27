class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rmax = []
        cmax = []
        for i in grid:
            rmax.append(max(i))
        
        for i in zip(*grid[::-1]):
            cmax.append(max(i))
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ret += min(rmax[i], cmax[j]) - grid[i][j]
        return ret
