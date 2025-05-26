class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxind=0
        for i in range(len(nums)):
            if i>maxind:
                return False
            maxind=max(i+nums[i],maxind)
            if maxind>=len(nums)-1:
                return True
        return True
        