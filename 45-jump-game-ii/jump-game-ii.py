class Solution:
    def jump(self, nums: list[int]) -> int:
        maxgo=0
        curr_max=0
        count=0
        for i in range(len(nums)):
            
            if curr_max<i:
                count+=1
                curr_max=maxgo
            if curr_max>=len(nums)-1:
                return count

            maxgo=max(maxgo,i+nums[i])

        
        