class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        self.target = target
        index = self.binarySearch(nums, 0, len(nums) - 1)
        if index == -1:
            return [-1, -1]
        
        first = self.getFirst(nums, index)
        last = self.getLast(nums, index)
        return [first, last]
    
    def binarySearch(self, nums, a, b):
        if nums[a] == self.target:
            return a
        elif nums[b] == self.target:
            return b
        elif a >= b:
            return -1
        
        mid = (a + b) // 2
        
        if nums[mid] == self.target:
            return mid
        elif nums[mid] > self.target:
            return self.binarySearch(nums, a, mid - 1)
        else:
            return self.binarySearch(nums, mid + 1, b)
        
    def getFirst(self, nums, index):
        while index >= 0 and nums[index] == self.target:
            index -= 1
            
        return index + 1
    
    def getLast(self, nums, index):
        while index < len(nums) and nums[index] == self.target:
            index += 1
            
        return index - 1
    
