from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def f(i,sub):
            if i==len(nums):
                result.append(sub[:])
                return 
            
            sub.append(nums[i])
            f(i+1,sub)
            sub.pop()
            f(i+1,sub)
        

        f(0,[])
        return result
        