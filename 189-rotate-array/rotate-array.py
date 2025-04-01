class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        self.rev(0,len(nums)-k-1,nums)
        self.rev(len(nums)-k,len(nums)-1,nums)
        self.rev(0,len(nums)-1,nums)
    
    def rev(self,i,j,nums):
        while(i<=j):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
        
        

        
        