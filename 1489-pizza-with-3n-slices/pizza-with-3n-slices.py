class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        k=len(slices)//3
        def find(arr):
            dp=[[-1e9]*(k+1) for _ in range(len(arr)+1)]
            for i in range(len(arr)):
                dp[i][0]=0
            
            dp[1][1]=arr[0]
            for i in range(2,len(arr)+1):
                for j in range(1,k+1):
                    dp[i][j]=max(dp[i-1][j],dp[i-2][j-1]+arr[i-1])
            return dp[len(arr)][k]


        first=find(slices[:len(slices)-1])
        second=find(slices[1:])
        return max(first,second)
        