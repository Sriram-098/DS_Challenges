from queue import PriorityQueue
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq=PriorityQueue()
        for i in nums:
            pq.put(i)
        count=0
        while not pq.empty() and pq.qsize()>1:
            if(pq.queue[0]<k):
                
                ele1=pq.get()
                ele2=pq.get()
                s=min(ele1,ele2)*2 +max(ele1,ele2)
                pq.put(s)
                count=count+1
            else:
                break
        return count






        