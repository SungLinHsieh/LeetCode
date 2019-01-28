class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        if len(nums1)>=len(nums2):
            long, short = nums1, nums2
        else:
            long, short = nums2, nums1
        """
        special cases
        """
        n = len(long)
        m = len(short)
        if m == 0:
            return self.SingleMedian(long)
        elif short[-1] <= long[0]:
            return self.SingleMedian(short+long)
        elif short[0] >= long[-1]:
            return self.SingleMedian(long+short)
        short_lb, short_ub = 0, m
        while(1):
            cut_short = (short_lb + short_ub)//2
            cut_long = (m+n)//2 - cut_short
            if cut_short < m and long[cut_long - 1] > short[cut_short]:
                short_lb = cut_short + 1
            elif cut_short > 0 and short[cut_short - 1] > long[cut_long]:
                short_ub = cut_short - 1
            else:
                if cut_short == m:
                    min_right = long[(n-m)//2]
                    max_left  = max(long[(n-m)//2-1], short[m-1])
                elif cut_short == 0:
                    min_right = min(long[(m+n)//2], short[0])
                    max_left = long[(m+n)//2-1]
                else:
                    min_right = min(long[cut_long], short[cut_short])
                    max_left = max(long[cut_long-1], short[cut_short-1])
            
                if (m+n)%2 == 1:
                    return min_right
                else:
                    return (max_left + min_right)/2
            
        
    def SingleMedian(self, nums):
        n = len(nums)
        if n%2 == 1:
            return nums[(n-1)//2]
        else:
            return (nums[n//2-1]+nums[n//2])/2
