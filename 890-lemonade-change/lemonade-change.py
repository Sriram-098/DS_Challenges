class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr=[0]*2
        for i in range(len(bills)):

            if bills[i]==5:
                arr[0]+=1
            elif bills[i]==10:
                arr[1]+=1
                
                if arr[0]>0:
                    arr[0]-=1
                
                else:
                    return False    
            else:
                if arr[1]>0 and arr[0]>=1:
                    arr[1]-=1
                    arr[0]-=1
                elif arr[0]>=3:
                    arr[0]-=3

                else:
                    return False
        return True
                
                

                
        