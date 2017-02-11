class Solution(object):
    def twoSum(self, numbers, target):
        u = len(numbers)-1
        l = 0
        while numbers[u]+numbers[l]!=target:
            if numbers[u]+numbers[l]<target:
                l=l+1
            else:
                u=u-1
        return [l+1,u+1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """