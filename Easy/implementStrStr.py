class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle not in haystack:
            return -1
        
        for index, item in enumerate(haystack):
            if item == needle[0]:
                try:
                    if haystack[index:index+len(needle)] == needle:
                        return index
                except:
                    return -1
