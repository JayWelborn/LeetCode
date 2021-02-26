class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = -inf
        for customer in accounts:
            maxWealth = max(sum(customer), maxWealth)
            
        return maxWealth
