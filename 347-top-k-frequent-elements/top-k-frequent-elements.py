class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #dict
        d=dict()
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]]+=1
            else:
                d[nums[i]]=1
        
        x=list(sorted(d.items(),key=lambda x:x[1],reverse=True))
        print(x)
        res=[]
        for i in range(k):
            res.append(x[i][0])
        return res
        


        
        
        

        
        