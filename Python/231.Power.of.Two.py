class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        Max = 2147483648
        if n <=0:
            return False
        else:
            return Max%n == 0
