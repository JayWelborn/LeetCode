class Solution:
    def removeDuplicates(self, S: str) -> str:
        ret = []
        for c in S:
            if not ret:
                ret.append(c)
            elif ret[-1] == c:
                ret.pop()
            else:
                ret.append(c)
        return ''.join(ret)
        
