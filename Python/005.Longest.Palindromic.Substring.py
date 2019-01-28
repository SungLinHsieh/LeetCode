class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        t = ['$']*(2*n+1)
        for i in range(n):
            t[2*i+1] = s[i]
        t = ''.join(t)
        z = self.z(t)
        index = z.index(max(z))
        pail = t[index-z[index]+1:index+z[index]-1]
        return pail.replace('$','')
        
    def z(self, s):
        n = len(s)
        z = [None] * n
        z[0] = 1
        L, R = 0, 0
        for i in range(1,n):
            if R < i or z[2*L-i] == R - i + 1:
                z[i] = self.findPail(s, i, i) if R < i else R - i + 1+ self.findPail(s, 2*i-R-1, R+1)
                L, R = i, i + z[i] - 1
            else:
                z[i] = min(z[2*L-i], R - i + 1)
        return z
    def findPail(self, s, l, r):
        i = 0
        n = len(s)
        while l-i>=0 and r+i < n and s[l-i] == s[r+i]:
            i += 1
        return i
