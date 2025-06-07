class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def backtrack(start,nums,path):
            if len(path)>=2:
                if path not in ans:
                    if path[-1]>=path[-2]:
                        ans.append(path[:])
                    else:
                        return 
            
            if start==len(nums):
                return 
            


            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,nums,path)
                path.pop()




        backtrack(0,nums,[])
        return ans
        