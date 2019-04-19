class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = []
        for i in range(numRows):
            row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(pascals[i-1][j-1] + pascals[i-1][ j])
            pascals.append(row)
            
        return pascals
