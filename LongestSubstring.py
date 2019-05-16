class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j, answer = 0, 0, 0
        window = set()
        while (i < len(s) and j < len(s)):
            if s[j] not in window:
                window.add(s[j])
                j += 1
                answer = max(answer, j - i)
            else:
                window.remove(s[i])
                i += 1
        return answer
