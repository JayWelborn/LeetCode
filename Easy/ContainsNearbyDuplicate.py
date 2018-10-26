class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        vals = {}
        for index, item in enumerate(nums):
            if item in vals and index - vals[item] <= k:
                return True
            vals[item] = index
            
        return False
 
