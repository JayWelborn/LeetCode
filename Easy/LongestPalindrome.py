class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        for char in s:
            chars[char] = chars.get(char, 0) + 1
        
        length = 0
        oddball = 0
        for char in chars:
            if chars[char] % 2 == 0:
                length += chars[char]
            else:
                length += chars[char] - 1
                oddball = 1
                
        return length + oddball
        
