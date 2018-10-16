class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
        
        x = abs(x)
        rev = int(str(x)[::-1])
        
        if rev > 2**31 - 1 or rev*sign < -2**31:
            return 0
        
        return rev * sign
    
