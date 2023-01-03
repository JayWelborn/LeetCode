class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0
        last_index = len(nums) - 1

        for index, item in enumerate(nums):
            if index > furthest:
                return False
            furthest = max(furthest, index + item)
            

        return furthest >= last_index
