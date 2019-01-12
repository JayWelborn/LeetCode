class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(A)
        cols = len(A[0])
        for i in range(rows):
            for j in range(cols // 2):
                A[i][j], A[i][cols - j - 1] = A[i][cols - j - 1], A[i][j]
        
        for i in range(rows):
            for j in range(cols):
                A[i][j] = abs(A[i][j] - 1)
                
        return A
        
