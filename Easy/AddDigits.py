class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        ret = 11
        while(ret >= 10):
            ret = 0
            while(num):
                ret += num % 10
                num //= 10
            num = ret
            
        return ret
