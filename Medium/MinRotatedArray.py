class Solution:
    def findMin(self, nums: List[int]) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1)
    
    def binarySearch(self, nums, a, b):
        
        if nums[a] <= nums[b]:
            return nums[a]
        mid = (a + b) // 2
        
        if a < mid < b and nums[mid] < nums[mid - 1] and nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif mid == b and nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        if nums[mid] > nums[b]:
            return self.binarySearch(nums, mid + 1, b)
        return self.binarySearch(nums, a, mid - 1)
        
