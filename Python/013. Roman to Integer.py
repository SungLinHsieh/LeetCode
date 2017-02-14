class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        D = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        s=list(s)
        n = 0
        for i in range(len(s)):
            if i < len(s)-1 and D[s[i]]<D[s[i+1]]:
                n = n - D[s[i]]
            else:
                n = n + D[s[i]]
        return n
        