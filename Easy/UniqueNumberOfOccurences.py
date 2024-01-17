class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        for item in arr:
            counter[item] += 1
        
        return len(counter.values()) == len(set(counter.values()))
