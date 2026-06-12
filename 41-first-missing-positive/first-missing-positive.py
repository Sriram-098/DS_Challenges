class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        r=0
        while r<len(nums):
            element=nums[r]
            pos=element-1

            if element>0 and element<=len(nums):
                if nums[pos]!=element:
                    nums[pos],nums[r]=nums[r],nums[pos]
                    continue
            r+=1

        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1

        



        