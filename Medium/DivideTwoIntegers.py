from operator import xor

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_VAL = -2147483648
        MAX_VAL = 2147483647

        is_negative = xor(dividend < 0, divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        if divisor == 1:
            if dividend == MIN_VAL and is_negative:
                return MAX_VAL
            else:
                return min(MAX_VAL, -dividend if is_negative else dividend)
        
        result = 0
        
        while dividend >= divisor:
            x = 0
            while dividend - (divisor << 1 << x) >= 0:
                x += 1
            result += 1 << x
            dividend -= divisor << x
        
        return -result if is_negative else result
