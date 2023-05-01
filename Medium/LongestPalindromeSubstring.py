from collections import defaultdict

class Solution:         
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
          return s
        
        cache = defaultdict(lambda: False)
        answer = s[0]

        for i in range(len(s)):
          cache[(i, i)] = True

        for end in range(len(s)):
          for start in range(end):
            if s[start] == s[end] and (start + 1 == end or cache[(start + 1, end - 1)]):
              cache[(start, end)] = True
              if len(s[start:end+1]) > len(answer):
                answer = s[start:end+1]

        return answer
