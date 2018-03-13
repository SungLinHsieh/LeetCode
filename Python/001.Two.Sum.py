class Solution(object):
    def twoSum(self, nums, target):
        m = min(nums)
        l = [False]*(target+1-2*m)
        n = [-1]*(target+1-2*m)
        for i in range(len(nums)):
            if nums[i]<=target-m:
                if l[target - nums[i]-m]==True:
                    return[n[target - nums[i]-m] ,i]
                else:
                    l[nums[i]-m]=True
                    n[nums[i]-m]=i
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        