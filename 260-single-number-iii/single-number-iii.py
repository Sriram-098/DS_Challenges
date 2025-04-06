class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d=Counter(nums)
        ans=[]
        for i,j in d.items():
            if j==1:
                ans.append(i)

        return ans
        