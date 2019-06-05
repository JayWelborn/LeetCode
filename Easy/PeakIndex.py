class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        if A[0] > A[1]:
            return 0
        for i in range(1, len(A) - 1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                return i
        return len(A) - 1
