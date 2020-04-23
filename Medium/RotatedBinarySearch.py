# [0, 1, 2, 3, 4, 5]

# [5, 0, 1, 2, 3, 4]

# [4, 5, 0, 1, 2, 3]

# [3. 4. 5. 0. 1. 2]

# [2, 3, 4, 5, 0, 1]

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        self.nums = nums
        self.target = target
        return self.binarySearch(0, len(nums) - 1)
    
    def binarySearch(self, a, b):
        if a > b:
            return -1
        
        mid = (a + b) // 2
        print(a, mid, b)
        if self.nums[mid] == self.target:
            return mid
        
        if self.nums[mid] > self.nums[b]:
            if self.target < self.nums[mid] and self.target >= self.nums[a]:
                return self.binarySearch(a, mid - 1)
            return self.binarySearch(mid + 1, b)
        
        if self.nums[mid] < self.nums[a]:
            if self.target > self.nums[mid] and self.target <= self.nums[b]:
                return self.binarySearch(mid + 1, b)
            return self.binarySearch(a, mid - 1)
        
        if self.target > self.nums[mid]:
            return self.binarySearch(mid + 1, b)
        return self.binarySearch(a, mid -1)
