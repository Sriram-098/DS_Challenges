class Solution:
    def maximumUnits(self, box: List[List[int]], s: int) -> int:
       
                
                
            
        ans=0
        box=sorted(box,key=lambda x:x[1],reverse=True)
        
        for i in range(len(box)):
            print(box[i][0],s)
            if s>=box[i][0]:
                
                ans=ans+(box[i][0]*box[i][1])
                s-=box[i][0]
            elif s<box[i][0]:
                ans+=(s*box[i][1])
                break
            
        return ans

        
            

        