import math
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0:
            return 0
        front = 0
        end   = n-1
        for i in range(int(math.log(n,2))+2):
            j = (front+end)/2
            if citations[j]>= n-j:
                if front == end:
                    return n-j
                end = j
            else:
                if front == end:
                    return 0
                front = j+1
        
