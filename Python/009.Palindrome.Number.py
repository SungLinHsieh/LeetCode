class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            strlist = list(str(x))
            i = 0
            n = len(strlist)
            while(i < n//2):
                if strlist[i] != strlist[n-i-1]:
                    return False
                i = i + 1
            return True
