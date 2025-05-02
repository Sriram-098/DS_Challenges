class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        prefix_left=[0]*len(nums)
        prefix_right=[0]*len(nums)
        prefix_left[0]=nums[0]
        prefix_right[len(nums)-1]=nums[len(nums)-1]
        for i in range(1,len(nums)):
            prefix_left[i]=prefix_left[i-1]+nums[i]
        for i in range(len(nums)-2,-1,-1):
            prefix_right[i]=prefix_right[i+1]+nums[i]
        
        if len(nums)>=2 and prefix_right[1]==0:
            return 0
        
        for i in range(1,len(nums)):
            if i<len(nums)-1 and prefix_left[i-1]==prefix_right[i+1]:
                return i
        if len(nums) >=2 and prefix_left[len(nums)-2]==0:
            return len(nums)-1
            
        return -1

        