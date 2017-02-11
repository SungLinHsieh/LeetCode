class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s=list(s)
        for c in t:
            if c not in s:
                return c
            else:
                s.remove(c)