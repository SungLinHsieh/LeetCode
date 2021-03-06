class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == []:
            return 0
        p = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                p = p + prices[i+1] - prices[i]
        return p