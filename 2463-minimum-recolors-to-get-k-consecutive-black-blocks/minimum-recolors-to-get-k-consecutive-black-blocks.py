class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_of_w=0
        l=0
        r=0
        mini=100000007
        while r<len(blocks):
            if blocks[r]=="W":
                count_of_w+=1
            
            while((r-l+1)>k and l<r):
                #print(True)
                if blocks[l]=="W":
                    count_of_w-=1
                l+=1
            
            if((r-l+1)==k):
                
                mini=min(mini,count_of_w)
                print(count_of_w,r,mini)
                
            r+=1
        return  mini


        