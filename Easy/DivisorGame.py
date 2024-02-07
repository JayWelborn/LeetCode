import math

class Solution:
    alice_wins = False
    def divisorGame(self, n: int) -> bool:
        while n > 1:
            for x in range(1, math.ceil(math.sqrt(n))):
                if n % x == 0:
                    self.alice_wins = not self.alice_wins
                    n = n - x
                    break
        
        return self.alice_wins
