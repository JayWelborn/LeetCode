class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        chars = []
        openers = {'(': 1, '{': 2, '[': 3}
        closers = {')': 1, '}': 2, ']': 3}
        for ch in s:
            if ch in openers:
                chars.append(ch)
            elif ch in closers:
                if len(chars) == 0:
                    return False
                last = chars.pop()
                if last not in openers or openers[last] != closers[ch]:
                    return False
        return len(chars) == 0
