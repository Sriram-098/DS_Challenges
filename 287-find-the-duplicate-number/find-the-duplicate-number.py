class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i=0
        while i<len(nums):
            place=nums[i]-1
            if place>=0 and place <=len(nums):
                if nums[i]!=nums[place]:
                    nums[i],nums[place]=nums[place],nums[i]
                    continue   
            i+=1
        
        for k in range(len(nums)):
            if nums[k]!=k+1:
                return nums[k]

                
    
        
        