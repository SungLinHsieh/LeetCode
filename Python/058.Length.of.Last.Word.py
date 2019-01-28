class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_space =0
        start = 0
        if len(s) ==0:
            return 0
        for i in range(len(s)-1,-1,-1):
            if start == 0 and s[i] !=" ":
                start = 1
            elif start == 0 and s[i]==" " :
                num_space = num_space +1
            elif start == 1 and s[i]==" ":
                return len(s)-i-1-num_space
            if i ==0:
                return len(s)-num_space
