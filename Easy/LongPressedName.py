class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        for letter in typed:
            if letter == name[i]:
                i += 1
            if i == len(name):
                return True
        return False
