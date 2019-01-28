class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = list()
        keys = list()
        for s in strs:
            tmpdic = self.str2dic(s)
            found = False
            for i in range(len(keys)):
                if keys[i] == tmpdic:
                    ans[i].append(s)
                    found = True
            if not found:
                keys.append(tmpdic)
                ans.append([s])
        return ans
            
        
    def str2dic(self, s):
        d = dict()
        for c in s:
            if c not in d.keys():
                d[c] = 1
            else:
                d[c] += 1
        return d
