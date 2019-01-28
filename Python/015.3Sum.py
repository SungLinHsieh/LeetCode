class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums) < 3:
            return ans
        nums.sort()
        end = len(nums)
        i = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i]==nums[i-1]:
                i = i + 1
                continue
            j = i + 1
            k = end - 1
            while ( j < k ):
                if j > i + 1 and nums[j]==nums[j-1]:
                    j = j + 1
                    continue
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    ans.append([nums[i], nums[j], nums[k]])
                if s <= 0:
                    j = j + 1
                if s > 0 and j == i + 1:
                    end = end - 1
                    k = k - 1
                elif s >= 0:
                    k = k - 1
        return ans
                    
