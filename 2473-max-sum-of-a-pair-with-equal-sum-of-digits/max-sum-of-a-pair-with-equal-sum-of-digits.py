class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        new_arr=[str(i) for i in nums]
        print(new_arr)
        arr=[]
        for i in range(len(nums)):
            s=0
            for j in range(len(new_arr[i])):
                s+=int(new_arr[i][j])

            arr.append(s)

        #[9,7,9,4,7]

        print(arr)
        d=dict()
        maxi_sum=-1
        for i in range(len(arr)):
            if arr[i] not in d:
                d[arr[i]]=i

            else:
                
                prev_ind=d.get(arr[i])
                curr_sum=nums[i]+nums[prev_ind]
                maxi_sum=max(curr_sum,maxi_sum)
                if nums[prev_ind]<nums[i]:
                    d[arr[i]]=i

        return maxi_sum

            

            

            


        

    

