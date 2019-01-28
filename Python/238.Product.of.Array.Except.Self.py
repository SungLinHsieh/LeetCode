class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = [1]*len(nums)
        for i in range(1,len(nums)):
            ans[i] = ans[i-1]*nums[i-1]
        product = 1
        for i in range(len(nums)-2,-1,-1):
            product *= nums[i+1]
            ans[i] *= product
        return ans
