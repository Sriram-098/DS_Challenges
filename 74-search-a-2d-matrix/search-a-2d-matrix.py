class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        left=0
        right=len(matrix)-1
        while left<=right:
            i=(left+right)//2
            if matrix[i][0]<=target and matrix[i][len(matrix[0])-1]>=target:
                low=0
                high=len(matrix[0])-1
                while low<=high:
                    mid=(low+high)//2
                    if matrix[i][mid]==target:
                        return True
                    if target>matrix[i][mid]:
                        low=mid+1
                    else:
                        high=mid-1
                return False
            elif matrix[i][0]<=target:
                left=i+1
            else:
                right=i-1
        return False


            

        