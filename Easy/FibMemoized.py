class Solution:
    cache = {0: 0, 1: 1}
    def fib(self, N: int) -> int:
        cache = {0: 0, 1: 1}
        if N in self.cache.keys():
            return self.cache[N]
        else:
            self.cache[N] = self.find_fib(N)
        return self.cache[N]
            
    def find_fib(self, N):
        if N < 2:
            return N
        return self.fib(N - 1) + self.fib(N - 2)
        
