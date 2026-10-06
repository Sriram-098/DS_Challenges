class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:

        totalsum = sum(nums)

        if totalsum + target < 0 or (totalsum + target) % 2 != 0:
            return 0

        s = (totalsum + target) // 2

        dp = [[0] * (s + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = 1

        for i in range(1, len(nums) + 1):

            curr = nums[i - 1]

            for j in range( s + 1):

                dp[i][j] = dp[i - 1][j]

                if j >= curr:
                    dp[i][j] += dp[i - 1][j - curr]

        return dp[len(nums)][s]