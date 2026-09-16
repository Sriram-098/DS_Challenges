class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        i=0
        while i<len(nums):
            curr_num=nums[i]
            num_place=nums[i]-1

            if num_place>=0 and num_place<len(nums):
                if nums[i]!=nums[num_place]:
                    nums[num_place],nums[i]=nums[i],nums[num_place]
                    continue
            i+=1
        print(nums)
        
        for i in range(len(nums)):
            if nums[i]!=i+1:
                return i+1
        return len(nums)+1
                    


        