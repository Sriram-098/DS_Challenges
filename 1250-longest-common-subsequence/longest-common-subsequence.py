from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @lru_cache(None)
        def lcs(i,j):
            if i<0 or j<0:
                return 0
            if text1[i]==text2[j]:
                return 1+lcs(i-1,j-1)
            return max(lcs(i,j-1),lcs(i-1,j))


        return lcs(len(text1)-1,len(text2)-1)
        