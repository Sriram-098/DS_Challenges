class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        i=0
        for j in range(len(arr)):
            if arr[j]!=0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1

        
        