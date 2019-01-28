class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        allowed_numbers = [2, 3, 5]
        for allowed_number in allowed_numbers:
            while num % allowed_number == 0:
                num = num / allowed_number
        if num == 1:
            return True
        else:
            return False
