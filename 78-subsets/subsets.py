class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        sub=[]
        def f(i,nums,sub,ans):
            if i==len(nums):
                ans.append(sub[:])
                return

            sub.append(nums[i])
            f(i+1,nums,sub,ans)
            sub.pop()
            f(i+1,nums,sub,ans)




        f(0,nums,sub,ans)
        return ans

    
        
        