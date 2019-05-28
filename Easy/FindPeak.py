class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            peak = True
            if i > 0 and nums[i] < nums[i - 1]:
                peak = False
            elif i < len(nums) - 1 and nums[i] < nums[i + 1]:
                peak = False
            if peak:
                return i
