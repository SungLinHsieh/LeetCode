class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx = 0
        n = len(nums)
        if n == 0:
            return 0
        for i in range(n):
            if nums[idx] != nums[i]:
                idx +=1
                nums[idx] = nums[i]
        return idx+1
