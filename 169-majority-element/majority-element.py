class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d=dict()
        maxi=0
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1

            maxi=max(maxi,d[nums[i]])
        for k,v in d.items():
            if v==maxi:
                return k
        return -1
        

        