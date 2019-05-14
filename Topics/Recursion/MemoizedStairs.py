class Solution:
    cache = {}
    def climbStairs(self, n: int) -> int:
        if n in self.cache.keys():
            return self.cache[n]
        self.cache[n] = self.findSteps(n)
        return self.cache[n]
    
    def findSteps(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
