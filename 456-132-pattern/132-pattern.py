class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second=-1e9
        st=[]
        for i in range(len(nums)-1,-1,-1):
            if nums[i]<second:
                return True

            while st and nums[i]>st[-1]:
                second=st.pop()
            
            st.append(nums[i])
        return False