class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        self.m = matrix
        self.l = list()
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        i = j = 0
        RU = True

        while i < m  and j < n:
            if RU:
                (newi, newj) = self.ru(m,n,i,j)
            else:
                (newi, newj) = self.ld(m,n,i,j)
            i, j = newi, newj
            RU = not RU
        return self.l
    def ru(self,m,n,i,j):
        if j == 0 and i<n-1:
            for k in range(i+1):
                self.l.append(self.m[i-k][j+k])
            return (0,j+i+1)
        elif j== 0 and i >=n-1:
            for k in range(n):
                self.l.append(self.m[i-k][j+k])
            return (i-n+2, n-1)
        elif j<n-m:
            for k in range(m):
                self.l.append(self.m[i-k][j+k])
            return (0 , j+m)
        else:
            for k in range(n-j):
                self.l.append(self.m[i-k][j+k])
            return (m-n+j+1, n-1)
    def ld(self,m,n,i,j):
        if i == 0 and j<m-1:
            for k in range(j+1):
                self.l.append(self.m[i+k][j-k])
            return (i+j+1, 0)
        elif i== 0 and j >= m-1:
            for k in range(m):
                self.l.append(self.m[i+k][j-k])
            return (m-1, j-m+2)
        elif i<m-n:
            for k in range(n):
                self.l.append(self.m[i+k][j-k])
            return (i+n, 0)
        else:
            for k in range(m-i):
                self.l.append(self.m[i+k][j-k])
            return (m-1,n-m+i+1)
        
