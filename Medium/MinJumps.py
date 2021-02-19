class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        visited = set()
        limit = max(x, max(forbidden)) + a + b
        q = [(0, 0, False)]
        while q:
            position, jumps, backwards = q.pop(0)
            
            if position > limit or position < 0 or position in forbidden or (position, backwards) in visited:
                continue
            if position == x:
                return jumps
            
            q.append((position + a, jumps + 1, False))
            
            if not backwards:
                q.append((position - b, jumps + 1, True))
          
            visited.add((position, backwards))
