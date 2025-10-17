class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=[]
        def backtrack(i,sub,target):
            
            if target==0:
                result.append(sub[:])
                return
            if i==len(nums):
                return 

            
            if target>=nums[i]:
                sub.append(nums[i])
                backtrack(i,sub,target-nums[i])
                sub.pop()

            backtrack(i+1,sub,target)
           
             

    
                


        sub=[]
        backtrack(0,sub,target)
        return result




        