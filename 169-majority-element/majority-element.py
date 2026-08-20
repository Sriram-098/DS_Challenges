class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        canditate=0
        for i in range(len(nums)):
            if count==0:
                canditate=nums[i]
                count=1
            elif nums[i]==canditate:
                count+=1
            else:
                count-=1

        return canditate
        
        