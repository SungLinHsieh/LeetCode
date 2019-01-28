class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        poss = [None]*(target+1)
        mod_cands = list()
        for num in candidates:
            if num <= target:
                mod_cands.append(num)
                poss[num] = [[num]]
        if mod_cands == []:
            return []
        for i in range(target+1):
            if poss[i] == None:
                poss[i] = []
        for i in range(min(mod_cands)+1,target+1):
            for num in mod_cands:
                if i >= num and poss[i-num] != []:
                    for comb in poss[i-num]:
                        if num <= comb[0]:
                            poss[i].append([num]+comb)
        return poss[target]
