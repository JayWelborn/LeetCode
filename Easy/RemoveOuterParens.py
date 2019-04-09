class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ret = ""
        stack = []
        for ch in S:
            if len(stack) == 0:
                stack.append(ch)
            elif ch == "(":
                stack.append(ch)
                ret += ch
            else:
                stack.pop()
                if len(stack) > 0:
                    ret += ch
        return ret
