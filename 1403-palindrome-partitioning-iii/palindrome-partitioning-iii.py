class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)

        # Helper to compute cost to make substring palindrome
        def cost(l, r):
            changes = 0
            while l < r:
                if s[l] != s[r]:
                    changes += 1
                l += 1
                r -= 1
            return changes

        from functools import lru_cache

        @lru_cache(None)
        def f(start, k_left):
            if start == n and k_left == 0:
                return 0
            if start == n or k_left == 0:
                return float("inf")

            ans = float("inf")
            for end in range(start, n):
                curr_cost = cost(start, end)
                ans = min(ans, curr_cost + f(end + 1, k_left - 1))
            return ans

        return f(0, k)
