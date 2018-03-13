class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        news = list()
        ip = list(s)
        l = len(s)
        for i in range(numRows):
            index = i
            while index < l:
                news.append(ip[index])
                index = index + 2*(numRows-i)-2
                if i == 0 or i == numRows-1:
                    index = index + 2*i
                    continue
                elif index >= l:
                    break
                else:
                    news.append(ip[index])
                    index = index + 2*i
        return ''.join(news)

d = Solution()
d.convert("A",1)
