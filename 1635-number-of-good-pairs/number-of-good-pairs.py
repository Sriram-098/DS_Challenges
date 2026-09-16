class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        ans=0
        for i in range(len(nums)):
            if nums[i] in freq:
                ans+=freq[nums[i]]
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        return ans

        