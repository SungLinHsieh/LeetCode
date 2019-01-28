class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if height == []:
            return 0
        globalmax = max(height)
        index = height.index(globalmax)
        
        localmax = height[0]
        h = 0
        tmp = 0
        
        for peak in height[:index+1]:
            if peak < localmax:
                tmp  = tmp+(localmax - peak)
            else:
                h = h+tmp
                tmp = 0
                localmax = peak
        localmax = height[-1]
        tmp = 0
        for peak in height[-1:None if index ==0 else index-1:-1]:
            if peak < localmax:
                tmp = tmp+(localmax - peak)
            else:
                h = h+tmp
                tmp = 0
                localmax = peak
        return h
