class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        tmp=list()
        tmpp=triangle[-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                tmp.append(triangle[i][j]+min(tmpp[j],tmpp[j+1]))
            tmpp = tmp
            tmp = list()
        return tmpp[0]
