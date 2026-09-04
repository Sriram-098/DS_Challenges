class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        totalsum=sum(nums)
        def kadenes_mini(arr):
            curr_mini=0
            mini=1e9
            for i in range(len(arr)):
                curr_mini+=arr[i]
                if curr_mini<mini:
                    mini=curr_mini
                if curr_mini>0:
                    curr_mini=0
            return mini
        def kadenes_maxi(arr):
            curr_sum=0
            max_sum=-1e9
            for i in range(len(arr)):
                curr_sum+=arr[i]
                #print(max_sum)
                if curr_sum>max_sum:
                    max_sum=curr_sum
                if curr_sum<0:
                    curr_sum=0
            return max_sum
        min_sum=kadenes_mini(nums)
        maxsum=kadenes_maxi(nums)

        
        print(maxsum,min_sum)

        if maxsum<0:
            return maxsum
        return max(totalsum-min_sum,maxsum)