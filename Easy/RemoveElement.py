# [1, 2, 3, 4, 4, 5]
# [1, 2, 3, 5, 4, 5], elem_count = 4

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write_index = 0
        elem_count = 0
        for read_index in range(len(nums)):
            if nums[read_index] != val:
                nums[write_index] = nums[read_index]
                elem_count += 1
                write_index += 1
        
        return elem_count
