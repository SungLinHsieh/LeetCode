class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        ans = []
        n = len(digits)
        map = dict()
        beg = 97
        for i in range(2,10):
            c = 4 if i == 7 or i == 9 else 3
            map[str(i)] = [chr(beg+j) for j in range(c)]
            beg += c
        def gen(s = '', i = 0):
            if i == n:
                ans.append(s)
                return
            else:
                for ch in map[digits[i]]:
                    gen(s+ch, i+1)
        gen()
        return ans
        
