class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        sets = set()
        for c in list(s):
            if len(sets) == 0 or c not in sets:
                sets.add(c)
            elif c in sets:
                l = l+2
                sets.remove(c)
        if len(sets) >0:
            l = l+1
        return l