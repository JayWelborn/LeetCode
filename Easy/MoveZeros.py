class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for index, num in enumerate(nums):
            if num != 0:
                nums[non_zero], nums[index] = nums[index], nums[non_zero]
                non_zero += 1
