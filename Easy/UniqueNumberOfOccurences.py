class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = defaultdict(int)
        for item in arr:
            counter[item] += 1

        count_set = set()
        
        for count in counter.values():
            if count in count_set:
                return False
            count_set.add(count)
        
        return True
