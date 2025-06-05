class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        sub=[]
        nums.sort()
        def f(i,nums,target,sub):
            if target==0:
                ans.append(sub[:])
                return 

            for j in range(i,len(nums)):
                if j>i and nums[j]==nums[j-1]:
                    continue
                if target<nums[j]:
                    break
                
                sub.append(nums[j])
                f(j+1,nums,target-nums[j],sub)
                sub.pop()

                    


        f(0,nums,target,sub)
        return ans
        