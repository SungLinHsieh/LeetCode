class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        LeftMax = 0
        RightMax = 0
        LeftIndex, RightIndex = 0, n-1
        MaxArea = 0
        while (LeftIndex < RightIndex):
            if height[LeftIndex] < LeftMax:
                LeftIndex += 1 
                continue
            else:
                LeftMax = height[LeftIndex]
            if height[RightIndex] < RightMax:
                RightIndex -=1
                continue
            else:
                RightMax = height[RightIndex]
            if height[LeftIndex] < height[RightIndex]:
                CurrentArea = (RightIndex-LeftIndex)*height[LeftIndex]
                LeftIndex += 1 
            elif height[LeftIndex] > height[RightIndex]:
                CurrentArea = (RightIndex-LeftIndex)*height[RightIndex]
                RightIndex -=1
            else:
                CurrentArea = (RightIndex-LeftIndex)*height[LeftIndex]
                LeftIndex += 1 
                RightIndex -=1
            if CurrentArea > MaxArea:
                MaxArea = CurrentArea
        return MaxArea
            
                
