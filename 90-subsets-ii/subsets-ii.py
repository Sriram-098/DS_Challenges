class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]


        def backtrack(i,sub):
            if i==len(nums):
                if sub[:] not in ans:
                    ans.append(sub[:])
                return 
                



            sub.append(nums[i])
            backtrack(i+1,sub)
            sub.pop()
            backtrack(i+1,sub)


        backtrack(0,[])
        return ans
        