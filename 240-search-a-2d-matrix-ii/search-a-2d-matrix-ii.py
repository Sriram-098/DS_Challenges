class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        high=len(matrix)-1
        for mid in range(len(matrix)):
            
            if target>=matrix[mid][0] and target<=matrix[mid][len(matrix[0])-1]:
                new_low=0
                new_high=len(matrix[0])-1
                while(new_low<=new_high):
                    new_mid=(new_low+new_high)//2
                    if matrix[mid][new_mid]==target:
                        return True
                    elif matrix[mid][new_mid]>target:
                        new_high=new_mid-1
                    else:
                        new_low=new_mid+1


        return False
        