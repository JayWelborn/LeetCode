class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        results = {}
        majority_length = len(nums) / 2
        for num in nums:
            if num in results:
                results[num] += 1
            else:
                results[num] = 1
            
            if results[num] > length / 2:
                return num
