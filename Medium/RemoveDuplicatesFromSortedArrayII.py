from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, write_index = 0, 0
        cache = defaultdict(int)

        for read_index, num in enumerate(nums):
            if cache[num] == 2:
                continue
            cache[num] += 1
            nums[write_index] = num
            write_index += 1
            k += 1
        
        return k
