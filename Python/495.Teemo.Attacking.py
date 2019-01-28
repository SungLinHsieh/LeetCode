class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if timeSeries == []:
            return 0
        time = 0
        for i in range(len(timeSeries)-1):
            time = time + min(duration, timeSeries[i+1]-timeSeries[i] )
        return time + duration
