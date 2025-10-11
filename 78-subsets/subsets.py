from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for i in range(len(nums)+1):
            for sub in combinations(nums,i):
                result.append(list(sub))
        return result
        