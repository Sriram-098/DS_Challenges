class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxsum=0
        currsum=0
        for i in range(len(nums)):
            currsum+=nums[i]
            if(currsum>maxsum):
                maxsum=currsum
            if(currsum<0):
                currsum=0
        
        currsum=0
        minsum=1e9
        for i in range(len(nums)):
            currsum+=nums[i]
            if(currsum<minsum):
                minsum=currsum
            if(currsum>0):
                currsum=0
        return max(abs(minsum),maxsum)
            



        
        