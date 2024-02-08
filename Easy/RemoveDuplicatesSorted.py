class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_set = set()
        write_index = 0
        for read_index, num in enumerate(nums):
            if not num in num_set:
                num_set.add(num)
                nums[write_index] = num
                write_index += 1
        
        return len(num_set)
