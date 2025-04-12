class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d={"b":0 ,"a":0,"l":0,"o":0,"n":0}
        x="balon"
        for i in range(len(text)):
            if text[i] in x:
                if text[i] in d:
                    d[text[i]]+=1
                else:
                    d[text[i]]=1
        print(d)
        min1=min(d.values())
        min2=min(d.get('l'),d.get('o'))

        if min1*2<=min2:
            return min1
        return min2//2
        

        
                
            
                

        
        
        