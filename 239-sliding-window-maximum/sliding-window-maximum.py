class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        st=deque()
        
        ans=[]
        
        for i in range(len(nums)):
            if st and i-k>=st[0]:
                st.popleft()
            # print(st)
            while st and nums[st[-1]]<nums[i]:
                st.pop()
            st.append(i)
            if i>=k-1:
                ans.append(nums[st[0]])
        return ans


                