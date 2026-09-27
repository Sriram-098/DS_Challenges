from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        s=Counter(nums)
        q=PriorityQueue()
        for x,v in s.items():
            q.put((-v,x))

        ans=[]
        print(q.queue)
        while k>0:
            
            a,b=q.get()
            ans.append(b)
            
            k-=1
        return ans
        

        