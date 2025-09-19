class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxgo=0
        for i in range(len(nums)):
            if i>maxgo:
                return False
            maxgo=max(maxgo,i+nums[i])
        return True
        