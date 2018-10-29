class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ret_list = [0] * length
        product = 1
        for i in range(length):
            ret_list[i] = product
            product *= nums[i]
        
        product = 1
        for i in range(length - 1, -1, -1):
            ret_list[i] *= product
            product *= nums[i]
            
        return ret_list
        
