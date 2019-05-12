class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        vals = {}
        for item in A:
            if item in vals:
                return item
            vals[item]=1
