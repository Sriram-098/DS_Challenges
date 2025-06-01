class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        q=deque()
        dp=[0]*len(nums)
        q.append(0)
        for i in range(len(nums)):
            if q[0]<i-k:
                q.popleft()
            dp[i]=nums[i]+dp[q[0]]

            while q and dp[i]>=dp[q[-1]]:
                q.pop()
            q.append(i)

        return dp[-1]