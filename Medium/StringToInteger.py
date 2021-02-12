class Solution:
    MIN_SIZE = -2147483648
    MAX_SIZE = 2147483647
    
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        if not s:
            return 0
        negative = s[0] == '-'
        if negative or s[0] == '+':
            s = s[1:]
        ret = 0
        
        for i in range(len(s)):
            asciiValue = ord(s[i])
            if asciiValue < 48 or 57 < asciiValue:
                break
            ret *= 10
            ret += asciiValue - 48

        if negative:
            ret = max(self.MIN_SIZE, -ret)
        else:
            ret = min(self.MAX_SIZE, ret)

        return ret
        
