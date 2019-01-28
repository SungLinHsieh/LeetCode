import math

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result = ""
        l = range(1,n+1)
        for i in range(n-1,-1,-1):
            index = int(math.ceil(1.0*k/math.factorial(i)))-1
            result = result + str(l[index])
            l.remove(l[index])
            k = k-index*math.factorial(i)
        return result
            
