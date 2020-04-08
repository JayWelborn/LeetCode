class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dictionary = {}
        for n in sorted(nums):
            dictionary[n] = dictionary.get(n, 0) + 1
            
        smaller = 0
        for key, value in dictionary.items():
            dictionary[key] = smaller
            smaller += value
            
        return [dictionary[c] for c in nums]
        
