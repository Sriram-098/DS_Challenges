class Solution:
    def maxSubarraySumCircular(self, arr: List[int]) -> int:
        totalsum=sum(arr)
        maxsum=self.kadenes(arr)
        minsum=self.minkadenes(arr)
        if maxsum<0:
            return maxsum
        return max(maxsum,totalsum-minsum)
    def kadenes(self,arr):
        curr=0
        maxsum=-1e9
        for i in range(len(arr)):
            curr+=arr[i]
            if maxsum<curr:
                maxsum=curr
            if curr<0:
                curr=0
        return maxsum
        
    def minkadenes(self,arr):
        curr=0
        minsum=1e9
        for i in range(len(arr)):
            curr+=arr[i]
            if minsum>curr:
                minsum=curr
            if curr>0:
                curr=0
        return minsum
        
        

