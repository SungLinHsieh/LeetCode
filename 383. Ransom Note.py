class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r = list(ransomNote)
        m = list(magazine)
        for c in r:
            if c not in m:
                return False
            else:
                m.remove(c)
        return True
        