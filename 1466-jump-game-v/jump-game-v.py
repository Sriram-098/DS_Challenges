class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp=[-1]*len(arr)
        def dfs(i):
            if dp[i]!=-1:
                return dp[i]

            slot=1
            for j in range(1,d+1):
                go=i-j
                if go<0 or arr[go]>=arr[i]:
                    break
                
                slot=max(slot,1+dfs(go))
            
            for j in range(1,d+1):
                go=i+j
                if go>=len(arr) or arr[go]>=arr[i]:
                    break
                
                slot=max(slot,1+dfs(go))
            
            dp[i]=slot
            return dp[i]

        maxi=0
        for i in range(len(arr)):
            maxi=max(maxi,dfs(i))
        return maxi
        