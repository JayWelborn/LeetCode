class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = set()
        for x in nums:
            if x in ret:
                ret.remove(x)
            else:
                ret.add(x)
        
        return ret.pop()
