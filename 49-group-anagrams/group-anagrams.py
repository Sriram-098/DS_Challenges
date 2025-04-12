class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            x=tuple(sorted(strs[i]))
            if  x in d:
                d[x].append(strs[i])

            else:
                
                d[x]=[strs[i]]
        return list(d.values())
        