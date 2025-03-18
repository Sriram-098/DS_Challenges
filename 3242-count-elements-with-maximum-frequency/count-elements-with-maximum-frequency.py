class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d=dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]=d.get(nums[i])+1
            else:
                d[nums[i]]=1

        maxfre=0 
        for i in d.values():
            maxfre=max(maxfre,i)
        
        c=0
        for i in d.values():
            if i==maxfre:
                c+=1
        
        return c*maxfre


        