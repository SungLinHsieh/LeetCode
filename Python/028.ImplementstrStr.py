class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        z = self.z(needle+'$'+haystack)
        for i in range(len(needle)+1,len(haystack)+len(needle)+1):
            if z[i] ==len(needle):
                return i-len(needle)-1
        return -1
    def z(self, s):
        n = len(s)
        z = [None] * n
        z[0] = n
        L, R = 0, 0
        for i in range(1,n):
            if R < i or z[i-L] == R - i + 1:
                x = i if R < i else R + 1
                while( x < n and s[x] == s[x-i]):
                    x += 1
                z[i] = x-i
                if i < x:
                    L, R = i, x-1
            elif z[i-L] < R - i + 1:
                z[i] = z[i-L]
            else:
                z[i] = R - i + 1
        return z
