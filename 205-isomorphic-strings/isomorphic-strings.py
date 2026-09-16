class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        if len(t)!=len(s):
            return False
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]]=t[i]
        return True
            

        