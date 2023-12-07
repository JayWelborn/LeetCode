class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_index = 0
        dup_count = 0
        recent = None
        for current in nums:
            if recent == current:
                dup_count += 1
            else:
                dup_count = 0
            if dup_count > 1:
                continue
            nums[write_index] = current
            recent = current
            write_index += 1
          
        return write_index
