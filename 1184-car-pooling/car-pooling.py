class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        changes=[0]*1001
        for passengers,st,end in trips:
            changes[st]+=passengers
            changes[end]-=passengers

        curr=0
        for i in range(1001):
            curr+=changes[i]
            if curr>capacity:
                return False
        return True
            