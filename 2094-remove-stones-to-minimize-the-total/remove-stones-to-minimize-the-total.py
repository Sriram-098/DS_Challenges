from queue import PriorityQueue
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        pq=PriorityQueue()
        for i in range(len(piles)):
            pq.put((-piles[i]))

        while(k>0):
            num=-(pq.get())
            floor_num=num//2

            num-=floor_num
            pq.put((-num))
            k-=1

        ans=0
        for i in range(pq.qsize()):
            ans+=(-pq.get())
        return ans

        