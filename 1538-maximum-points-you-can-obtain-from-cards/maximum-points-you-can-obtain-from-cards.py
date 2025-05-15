class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        maxscore=0
        for i in range(k):
            maxscore += cardPoints[i]
        
        l=k-1
        r=len(cardPoints)-1
        maxi=0
        maxi=max(maxscore,maxi)
        while(l>=0):
            
            maxscore-=cardPoints[l]
            maxscore+=cardPoints[r]
            maxi=max(maxscore,maxi)
            l-=1
            r-=1
        return maxi




        