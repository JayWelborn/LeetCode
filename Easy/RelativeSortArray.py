class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        count = Counter(arr1)
        index = 0
        ret = []
        for n in arr2:
            ret[index:index + count[n]] = [n] * count[n]
            index += count[n]
            count[n] = 0
        
        for n in sorted(count.keys()):
            ret[index:index + count[n]] = [n] * count[n]
            index += count[n]
        
        return ret
