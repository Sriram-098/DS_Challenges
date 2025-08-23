class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x=Counter(nums)
        print(x)
        for k,v in x.items():
           
            if v>1:
                return k
        
        