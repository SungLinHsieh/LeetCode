class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        corr = {')':'(','}':'{',']':'['}
        que = list()
        for c in s:
            if c in corr.keys() and len(que)>0 and que[-1] == corr[c]:
                que.pop()
            elif c in corr.keys():
                return False
            else:
                que.append(c)
        if que == []:
            return True
        else:
            return False
