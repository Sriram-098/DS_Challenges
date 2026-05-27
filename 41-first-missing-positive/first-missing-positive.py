class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        r=0
        while (r<len(nums)):
            num=nums[r]
            pos=nums[r]-1
            if num>0 and num<len(nums):
                if num!=nums[pos]:
                    nums[r],nums[pos]=nums[pos],nums[r]
                    continue
            r+=1
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1



        