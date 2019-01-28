class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        def stolist(st,l):
            for c in st:
                l[ord(c)-97] += 1
            return l
        slist = stolist(s,[0]*26)
        tlist = stolist(t,[0]*26)
        for i in range(26):
            if slist[i] != tlist[i]:
                return False
        return True
        
