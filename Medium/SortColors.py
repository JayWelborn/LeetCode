class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = {}
        
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        for i in range(len(nums)):
            if i < counts.get(0, 0):
                nums[i] = 0
            elif i < counts.get(0, 0) + counts.get(1, 0):
                nums[i] = 1
            else:
                nums[i] = 2
