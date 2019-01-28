class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        Max = 2147483648
        if num <=0:
            return False
        else:
            return Max%num == 0 and math.sqrt(num).is_integer()
        
