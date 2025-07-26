class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d=dict()
        for i in range(len(strs)):
            key="".join(sorted(list(strs[i])))
            print(key)
            if key in d:
                d[key].append(strs[i])
            else:
                d[key]=[strs[i]]
        ans=[]
        for i in d.values():
            ans.append(i)
        return ans
        
        