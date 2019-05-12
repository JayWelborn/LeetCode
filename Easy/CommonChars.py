class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        common = {}
        for char in A[0]:
            if char in common:
                common[char] += 1
            else:
                common[char] = 1
            
        for word in A[1:]:
            for char in common:
                common[char] = min(word.count(char), common[char])
                
        chars = []
        for char, count in common.items():
            for i in range(count):
                chars.append(char)
        
        return chars
