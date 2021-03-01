class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        current = {}
        for item in items:
            current['type'] = item[0]
            current['color'] = item[1]            
            current['name'] = item[2]
            if current[ruleKey] == ruleValue:
                count += 1
        
        return count
