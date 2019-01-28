class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] > 9:
                if i == 0:
                    digits[0] -= 10
                    digits = [1] + digits
                else:
                    digits[i] -= 10
                    digits[i-1] += 1
        return digits
        
