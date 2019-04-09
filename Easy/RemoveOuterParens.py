class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        ret = ""
        
        for ch in S:
            if count == 0:
                count += 1
            elif ch == "(":
                count += 1
                ret += ch
            else:
                count -= 1
                if count != 0:
                    ret += ch
        
        return ret
                
