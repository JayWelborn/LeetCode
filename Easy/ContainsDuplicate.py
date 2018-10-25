class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vals = {}
        for x in nums:
            if x in vals:
                return True
            else:
                vals[x] = "true"
        return False
 
