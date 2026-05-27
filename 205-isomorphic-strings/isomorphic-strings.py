class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d={}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]]!=t[i]:
                    return False
            else:
                if t[i] not in d.values():
                    d[s[i]]=t[i]
                else:
                    return False
        return True


        