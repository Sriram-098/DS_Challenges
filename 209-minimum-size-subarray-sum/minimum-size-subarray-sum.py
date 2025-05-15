class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        maxlen=1e9
        s=0
        while(r<len(nums)):
            s+=nums[r]
            while(s>=target):
                maxlen=min(r-l+1,maxlen)
                print(maxlen)
                s-=nums[l]
                l+=1
            r+=1
        return maxlen if maxlen !=1e9 else 0


        