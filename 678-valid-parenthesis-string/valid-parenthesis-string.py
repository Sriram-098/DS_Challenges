from functools import lru_cache
class Solution:
    def checkValidString(self, s: str) -> bool:

        @lru_cache(maxsize=None)
        def dfs(i,count):
            if i==len(s):
                return count==0
            if count<0:
                return False

            if s[i]=="(":
                return dfs(i+1,count+1)
            elif s[i]==")":
                return dfs(i+1,count-1)
            else:
                return (dfs(i+1,count+1) or dfs(i+1,count-1) or dfs(i+1,count))





        return dfs(0,0)
        
        