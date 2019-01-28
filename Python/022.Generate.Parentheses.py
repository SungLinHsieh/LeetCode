class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def gen(s = '', l = 0, r = 0):
            if len(s) == 2*n:
                ans.append(s)
                return
            if l < n:
                gen(s+'(', l + 1, r)
            if l > r:
                gen(s+')', l, r+1)
        gen()
        return ans
        
