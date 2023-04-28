class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i_output = m + n - 1
        m -= 1
        n -=1

        while i_output >= 0:
            if m < 0:
                nums1[i_output] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[i_output] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[i_output] = nums1[m]
                m -= 1
            else:
                nums1[i_output] = nums2[n]
                n -= 1
            i_output -= 1
