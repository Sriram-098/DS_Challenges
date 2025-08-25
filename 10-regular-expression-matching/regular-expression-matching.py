from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def f(i,j):
            if i<0 and j<0:
                return True
            if i>=0 and j<0:
                return False
            if i<0 and j>=0:
                while j>=0:
                    if p[j]=='*':
                        j-=2
                    else:
                        return False
                    
                return True


            if p[j]=='.' or s[i]==p[j]:
                return f(i-1,j-1)
            if p[j]=='*':
                if j>0 and (p[j-1]==s[i] or p[j-1]=='.'):
                    return f(i,j-1) or f(i,j-2) or f(i-1,j)
                else:
                    return f(i,j-2)
                
            return False
        return f(len(s)-1,len(p)-1)