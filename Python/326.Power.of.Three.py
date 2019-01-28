class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Max3PowerInt = 1162261467
        if n <= 0:
            return False
        else:
            return Max3PowerInt%n ==0
