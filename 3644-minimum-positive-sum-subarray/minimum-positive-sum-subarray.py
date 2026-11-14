class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        mini = float('inf')

        for i in range(n):
            for j in range(l, r+1):
                if i+j <= n:
                    s = prefix[i+j] - prefix[i]

                    if s > 0:
                        mini = min(mini, s)

        return mini if mini != float('inf') else -1