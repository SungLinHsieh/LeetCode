class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        d=0
        for i in range(31):
            if x ==y:
                break
            if x%2 != y%2:
                d=d+1
            x=(x-x%2)/2
            y=(y-y%2)/2
        return d