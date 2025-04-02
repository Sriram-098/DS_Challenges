class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while(i<len(nums)):
            ele=nums[i]
            if(ele>0 and ele<=len(nums)):
                place=ele-1
                if(nums[place]!=ele):
                    
                    nums[place],nums[i]=nums[i],nums[place]
                    continue
            i+=1
        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
        