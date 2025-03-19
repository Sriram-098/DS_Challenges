class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l=0
        r=0
        operations=0
        while(r<len(nums)):

            if(nums[r]==0):
                if r+2<len(nums):
                    for i in range(r,r+3):
                        nums[i]=1-nums[i]
                    operations+=1
            r+=1
        
        for i in range(len(nums)):
            if nums[i]==0:
                return -1
        return operations


        