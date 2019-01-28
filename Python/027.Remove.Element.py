class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        count = 0
        while( i < n):
            if nums[i] == val:
                for j in range(i,n-1):
                    nums[j] = nums[j+1]
                n = n-1
                count = count +1
            else:
                i = i+1
        return n
