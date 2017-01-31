class Solution(object):
    def findComplement(self, num):
        p = 2
        while p<=num:
            p=p*2
        return p-num-1
        """
        :type num: int
        :rtype: int
        """