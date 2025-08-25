from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def f(i,j):
            if i<0 and j<0:
                return True
            if i>=0 and  j<0:
                return False
            if i<0 and j>=0:
                while j>=0:
                    if p[j]!='*':
                        return False
                    j-=1
                return True



            if p[j]=="?" or p[j]==s[i]:
                return f(i-1,j-1)
            if p[j]=='*':
                return f(i-1,j) or f(i,j-1)
            return False





        return f(len(s)-1,len(p)-1)
        