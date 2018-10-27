class Solution:
    def toLowerCase(self, string):
        """
        :type str: str
        :rtype: str
        """
        ret = []
        for c in string:
            cascii = ord(c)
            ret.append(chr(cascii + 32) if 65 <= cascii <= 95 else c)
        
        return ''.join(ret)


# Python Easy Way
# class Solution:
#     def toLowerCase(self, string):
#         """
#         :type str: str
#         :rtype: str
#         """
#         return string.lower()
