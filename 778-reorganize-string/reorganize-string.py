import queue
class Solution:
    def reorganizeString(self, s: str) -> str:
        d=Counter(s)
        pq=queue.PriorityQueue()
        for i,j in d.items():
            print(i,j)
            pq.put((-j,i))

        res=[]
        prevcount,prevchar=0,""
        while not pq.empty():
            count,char=pq.get()
            res.append(char)

            if prevcount<0:
                pq.put((prevcount,prevchar))
            
            prevcount,prevchar=count+1,char

        print(res)

        return ''.join(res) if len(res)==len(s) else ""
