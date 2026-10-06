class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: list[list[int]]) -> int:
        n = len(stations)

        dp = [0] * (n + 1)
        dp[0] = startFuel

        for i in range(n):
            pos, fuel = stations[i]

            for j in range(i + 1, 0, -1):
                if dp[j - 1] >= pos:
                    dp[j] = max(dp[j], dp[j - 1] + fuel)

        for j in range(n + 1):
            if dp[j] >= target:
                return j

        return -1