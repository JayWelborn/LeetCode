class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1 and not trust:
            return 1
        people = set()
        trusters = set()
        trusted_by = {}
        for truster, trustee in trust:
            people.add(truster)
            try:
                trusted_by[trustee].append(truster)
            except:
                trusted_by[trustee] = [truster]
                
        for key, value in trusted_by.items():
            if len(value) == N-1 and not key in people:
                return key
        return -1
