from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @lru_cache(None)
        def f(i,j):
            if i<0:
                return j
            if j<0:
                return i
            if word1[i]==word2[j]:
                return f(i-1,j-1)
            insert,delete,replace=1e9,1e9,1e9
            insert =1+f(i,j-1)
            delete=1+f(i-1,j)
            replace=1+f(i-1,j-1)
            return min(insert,delete,replace)



        return f(len(word1)-1,len(word2)-1)+1
        