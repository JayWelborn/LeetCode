class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        for i in S:
            if i in J:
                total = total + 1
        return total

