class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[-1,-1]
        d={}
        for i in range(len(nums)):
            if target-nums[i] in d:
                ans[0]=d[target-nums[i]]
                ans[1]=i
            else:
                d[nums[i]]=i
        return ans
        