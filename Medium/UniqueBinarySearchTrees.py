class Solution:

    treeCache = {}

    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        elif n in self.treeCache:
            return self.treeCache[n]

        total = 0
        for left in range(n):
            right = n - left - 1
            if left and right:
                total += self.numTrees(left) * self.numTrees(right)
            elif left:
                total += self.numTrees(left)
            elif right:
                total += self.numTrees(right)
        
        self.treeCache[n] = total
        return total
