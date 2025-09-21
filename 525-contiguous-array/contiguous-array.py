class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count=0
        d={0:-1}
        maxi=0
        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            if nums[i]==1:
                count+=1
            if count in d:
                maxi=max(maxi,i-d[count])

            else:
                d[count]=i
        return maxi
            

        