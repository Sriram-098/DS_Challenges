class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        

        i=0
        while i<len(nums):
            num=nums[i]
            place=nums[i]-1
            if num>0 and num<len(nums):
                if num!=nums[place]:
                    nums[i],nums[place]=nums[place],nums[i]
                    continue
            i+=1
        print(nums)
        for k in range(len(nums)):
            if nums[k]!=k+1:
                return k+1
        
        return len(nums)+1


        