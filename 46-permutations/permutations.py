from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for sub in permutations(nums):
            result.append(sub)
        return result
        

        