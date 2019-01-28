class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <3:
            return 0
        nums = [1]*n
        nums[1] = nums[0] = 0
        for i in range(2,int(n**(0.5))+1):
            if nums[i] == 1:
                for j in range(2,(n-1)//i+1):
                    nums[i*j] = 0
        return sum(nums)
