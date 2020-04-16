class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cache = {}
        highest_frequency = 0
        shortest_subarray = sys.maxsize
        for i in range(len(nums)):
            freq, first, last = cache.get(nums[i], [0, i, i])
            freq += 1
            last = i
            if freq > highest_frequency:
                highest_frequency = freq
                shortest_subarray = last - first + 1
            elif freq == highest_frequency:
                shortest_subarray = min(shortest_subarray, last - first + 1)
            cache[nums[i]] = [freq, first, last]
        return shortest_subarray
