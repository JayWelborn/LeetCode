class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        low = 0
        high = num
        mid = (low + high) // 2
        while low < high - 1:
            mid = int((low + high) // 2)
            square = mid * mid
            if square == num:
                return True
            elif square < num:
                low = mid
            else:
                high = mid
        return square == num
