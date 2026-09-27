from queue import PriorityQueue
import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        s=Counter(nums)
        heap=[]
        for key,val in s.items():
            heapq.heappush(heap,(val,key))

            if len(heap)>k:
                heapq.heappop(heap)

        return [key for val,key in heap]

        