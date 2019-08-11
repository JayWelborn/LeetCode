class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0
        
        digits_a = list(a)
        digits_b = list(b)
        
        while digits_a or digits_b or carry:
            if digits_a:
                carry += int(digits_a.pop())
            if digits_b:
                carry += int(digits_b.pop())
                
            res = str(carry % 2) + res
            carry //= 2
        
        if not res:
            res = '0'
        return res
