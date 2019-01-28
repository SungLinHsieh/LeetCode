class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = collections.Counter(nums)
        n = len(nums)
        for a in x:
            if x[a]>n/2:
                return a
