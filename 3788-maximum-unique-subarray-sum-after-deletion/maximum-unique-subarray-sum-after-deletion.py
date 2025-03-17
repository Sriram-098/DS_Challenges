class Solution:
    def maxSum(self, nums: List[int]) -> int:
        s=set()
        for i in range(len(nums)):
            if nums[i]>0:
                s.add(nums[i])
        return sum(s) if s else max(nums)
        

    

        