class Solution:
    def jump(self, nums: List[int]) -> int:
        maxgo=0
        count=0
        end=0
        jumps=0
        for i in  range(len(nums)-1):
            maxgo=max(maxgo,i+nums[i])
            if i==end:
                jumps+=1
                end=maxgo
                if end>=len(nums)-1:
                    break
            
        return jumps

        
        