class Solution:
    def getNum(self, old, j):
        if j == 0 or j > len(old) - 1:
            return 1
        else:
            return old[j - 1] + old[j]

    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            new_row = []
            for j in range(i + 1):
                new_row.append(self.getNum(row, j))
            row = new_row
        return row
