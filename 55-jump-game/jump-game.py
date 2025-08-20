class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxgo=0
        currgo=0
        for i in range(len(nums)):
            if maxgo<i:
                return False
            maxgo=max(maxgo,nums[i]+i)
            if maxgo>=len(nums)-1:
                return True
        return False
            
        
