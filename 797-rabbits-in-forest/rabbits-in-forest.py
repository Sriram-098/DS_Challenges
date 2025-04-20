class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        d=Counter(answers)
        ans=0
        for i,j in d.items():
            s=i+1
            ans+=math.ceil(j/s)*s
        return ans

            
        