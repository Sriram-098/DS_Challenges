class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        left=1
        right=1
        ans=-1e9
        for i in range(len(nums)):
            if left==0:
                left =1
            if right==0:
                right=1
            left=left*nums[i]
            right=right*nums[len(nums)-i-1]
            ans=max(ans,left,right)
        return ans
        
        