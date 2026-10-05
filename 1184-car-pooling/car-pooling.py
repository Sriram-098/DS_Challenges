class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:(x[1],x[2]))
        print(trips)
        i=1
        newcap=trips[0][0]
        start=trips[0][1]
        if trips[0][0]>capacity:
            return False
        l=0
        d={}
        d[(trips[0][1],trips[0][2])]=trips[0][0]
        while i<len(trips):
            for k,v in d.items():
                if k[1]<=trips[i][1]:
                    newcap-=d[k]
                    d[k]=0
            
            
            newcap+=trips[i][0]
            if newcap>capacity:
                return False
            if (trips[i][1],trips[i][2]) in d:
                d[(trips[i][1],trips[i][2])]+=trips[i][0]
            else:
                d[(trips[i][1],trips[i][2])]=trips[i][0]
            i+=1
        return True
            


    