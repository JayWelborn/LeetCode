class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        base = 2
        bit_count = [0, 1]
        for i in range(2, num + 1):
            bit_count.append(bit_count[i - base] + 1)
            if base * 2 <= i + 1:
                base *= 2
        return bit_count
