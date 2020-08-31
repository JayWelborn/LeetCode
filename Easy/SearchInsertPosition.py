class Solution(object):
    def searchInsertFastInPython(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for index, item in enumerate(nums):
            if item >= target:
                return index
        return index + 1
    
    
    def searchInsertNaive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.append(target)
        nums.sort()
        return nums.index(target)

    def searchInsertBinarySearchRecursive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums or len(nums) == 0:
            return 0
        
        def binarySearch(a, b, nums, target):
            if a >= b:
                return a
            mid = a + (b - a) // 2
            if nums[mid] >= target:
                return binarySearch(a, mid, nums, target)
            else:
                return binarySearch(mid + 1, b, nums, target)
        
        return binarySearch(0, len(nums), nums, target)
        
    def searchInsertBinarySearchIterative(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)
        while (left < right):
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        return left
