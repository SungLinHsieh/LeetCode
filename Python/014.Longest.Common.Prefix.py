class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ''
        n = len(strs)
        ans = strs
        while len(ans) > 1:
            m = len(ans)
            tmp = []
            for i in range(m//2):
                tmp.append(self.duocompare(ans[2*i],ans[2*i+1]))
            if m%2 == 1:
                tmp.append(ans[-1])
            ans = tmp
        return ans[0]
    def duocompare(self,s1,s2):
        if s1 == '' or s2 == '' or s1[0] != s2[0]:
            return ''
        for i in range(min(len(s1),len(s2))):
            if i == min(len(s1),len(s2))-1 or s1[i+1] != s2[i+1]:
                break
        return s1[:i+1]
