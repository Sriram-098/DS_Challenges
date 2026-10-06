from functools import lru_cache
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @lru_cache(None)
        def solve(i,n,s):
            if i==n:
                return 1
            ans=0
            if len(s)==0:
                ans+=solve(i+1,n,"a")% (10**9 + 7)
                ans+=solve(i+1,n,"e")% (10**9 + 7)
                ans+=solve(i+1,n,"i")% (10**9 + 7)
                ans+=solve(i+1,n,"o")% (10**9 + 7)
                ans+=solve(i+1,n,"u")% (10**9 + 7)
            if s==("a"):
                ans+=solve(i+1,n,"e")% (10**9 + 7)
            if s==("e"):
                ans+=solve(i+1,n,"a")% (10**9 + 7)
                ans+=solve(i+1,n,"i")% (10**9 + 7)
            if s==("i"):
                ans+=solve(i+1,n,"a")% (10**9 + 7)
                ans+=solve(i+1,n,"e")% (10**9 + 7)
                ans+=solve(i+1,n,"o")% (10**9 + 7)
                ans+=solve(i+1,n,"u")% (10**9 + 7)
            if s==("o"):
                ans+=solve(i+1,n,"i")% (10**9 + 7)
                ans+=solve(i+1,n,"u")% (10**9 + 7)
            if s==("u"):
                ans+=solve(i+1,n,"a")% (10**9 + 7)

            return ans% (10**9 + 7)

        return solve(0,n,"")






        