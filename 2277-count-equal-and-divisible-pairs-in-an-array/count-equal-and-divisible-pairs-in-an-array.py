class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    if ((i*j)/k)==((i*j)//k):
                        print(i,j)
                        ans+=1

        return ans
        