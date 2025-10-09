class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(i,j):
            if i>=j:
                return 
            
            mid=(i+j)//2
            merge(i,mid)
            merge(mid+1,j)
            conquer(i,mid,j)

        def conquer(s,mid,e):
            temp=[]
            i,j=s,mid+1
            while i<=mid and j<=e:
                if nums[i]<=nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
                
            while i<=mid:
                temp.append(nums[i])
                i+=1
            while j<=e:
                temp.append(nums[j])
                j+=1
            for k in range(len(temp)):
                nums[s+k]=temp[k]
            

        merge(0,len(nums)-1)
        return nums

        