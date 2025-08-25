from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cost(i,j):
            count=0
            while i<j:
                if s[i]!=s[j]:
                    count+=1
                i+=1
                j-=1
            return count
        @lru_cache(None)
        def f(start,k_left):
            if k_left==0 and start==len(s):
                return 0
            if k_left==0 or start==len(s):
                return 1e9
            mini=1e9
            for end in range(start,len(s)):
                costn=cost(start,end)
                mini=min(mini,costn+f(end+1,k_left-1))
            return mini
        
        return f(0,k)