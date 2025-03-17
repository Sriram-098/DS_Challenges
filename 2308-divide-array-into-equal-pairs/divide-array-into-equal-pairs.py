class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d=dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]=d.get(nums[i])+1
            else:
                d[nums[i]]=1
        
        for i in d.values():
            if i%2!=0:
                return False
        
        return True



        