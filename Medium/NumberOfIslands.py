class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numIslands = 0
        self.grid = grid
        self.islands = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in self.islands and grid[i][j] == "1":
                    numIslands += 1
                    self.addIsland(i, j)
        
        return numIslands
    
    def addIsland(self, i, j):
        self.islands[(i,j)] = 1
        if i > 0 and (i-1,j) not in self.islands and self.grid[i - 1][j] == "1":
            self.addIsland(i - 1, j)
        if i < len(self.grid) - 1 and (i+1,j) not in self.islands and self.grid[i + 1][j] == "1":
            self.addIsland(i + 1, j)
        if j > 0 and (i,j-1) not in self.islands and self.grid[i][j - 1] == "1":
            self.addIsland(i, j - 1)
        if j < len(self.grid[0]) - 1 and (i,j+1) not in self.islands and self.grid[i][j + 1] == "1":
            self.addIsland(i, j + 1)
