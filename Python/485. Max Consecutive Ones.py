class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        l=0
        m=0
        for i in nums:
            l=l*i+i
            if l>m:
                m=l
        return m
        """
        :type nums: List[int]
        :rtype: int
        """