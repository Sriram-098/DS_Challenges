from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq=PriorityQueue()
        for i in range(len(stones)):
            pq.put((-stones[i]))
        while pq.qsize()>1:
            first=-(pq.get())
            second=-(pq.get())
            if first==second:
                continue
            pq.put((-(first-second)))
        ans=[]
        if not pq.empty():
            x=-(pq.get())
            return x
        return 0
            

        