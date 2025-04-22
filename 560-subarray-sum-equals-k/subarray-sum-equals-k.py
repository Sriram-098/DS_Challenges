class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d=dict()
        d[0]=1
        count=0
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            rem=sum-k
            count+=d.get(rem,0)
            d[sum]=d.get(sum,0)+1
        return count


        
            
        