from functools import lru_cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def sub(i,j):
            if j<0:
                return 1
            if i<0:
                return 0
            
            if s[i]==t[j]:
                return sub(i-1,j-1)+sub(i-1,j)
            return sub(i-1,j)


        return sub(len(s)-1,len(t)-1)
        