class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        solution = {}
        for i in range(len(nums)):
            if nums[i] in solution:
                return [solution[nums[i]], i]
            else:
                solution[target - nums[i]] = i

