from collections import deque

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup, stack = {}, deque()
        for num in nums2[::-1]:
            while stack and num > stack[-1]:
                stack.pop()
            if stack:
                lookup[num] = stack[-1]
            stack.append(num)
        
        return [lookup.get(num, -1) for num in nums1]
