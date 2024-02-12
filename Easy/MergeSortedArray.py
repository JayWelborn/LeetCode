class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we must iterate in reverse, to avoid overwriting items we need from our array
        write_index = m + n - 1
        m -= 1
        n -= 1

        while write_index >= 0:
            if m < 0:
                nums1[write_index] = nums2[n]
                n -= 1
            elif n < 0:
                nums1[write_index] = nums1[m]
                m -= 1
            elif nums1[m] > nums2[n]:
                nums1[write_index] = nums1[m]
                m -= 1
            else:
                nums1[write_index] = nums2[n]
                n -= 1
            write_index -= 1

        return nums1
