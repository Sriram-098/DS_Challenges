class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddcount,prefixsum,mod=0,0,1_000_000_007
        for i in arr:
            prefixsum+=i
            oddcount+=prefixsum%2
        oddcount+=(len(arr)-oddcount)*oddcount
        return oddcount%mod



        