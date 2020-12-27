class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        self.memo = {}
        return self.recursiveDecodings(s)
    
    def recursiveDecodings(self, s):
        if len(s) == 0:
            return 1
        if s in self.memo:
            return self.memo[s]
        
        
        oneDigit = 0
        twoDigits = 0
        if int(s[:1]) != 0:
            oneDigit = self.recursiveDecodings(s[1:])
        if 10 <= int(s[:2]) <= 26:
            twoDigits = self.recursiveDecodings(s[2:])
            
        self.memo[s] = oneDigit + twoDigits
        return self.memo[s]
