class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        sub=[]
        def f(i,nums,target,sub):
            if target==0:
                ans.append(sub[:])
                return 

            if i==len(nums):
                if target==0:
                    ans.append(sub[:])
                return 

            if target>=nums[i]:
                sub.append(nums[i])
                f(i,nums,target-nums[i],sub)
                sub.pop()

            f(i+1,nums,target,sub)



        f(0,nums,target,sub)
        return ans
        