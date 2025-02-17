class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count=Counter(tiles)
        def recur():
            ans=0
            for i in count:
                if count[i]>0:
                    count[i]-=1
                    ans+=1
                    ans+=recur()
                    count[i]+=1
            return ans

        return recur()
        