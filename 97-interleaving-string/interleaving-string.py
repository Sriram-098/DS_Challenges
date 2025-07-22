class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=None)  # \U0001f448 Add memoization!
        def f(i, j, k):
            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if k == len(s3):
                return False

            first = False
            second = False

            if i < len(s1) and s1[i] == s3[k]:
                first = f(i + 1, j, k + 1)
            if j < len(s2) and s2[j] == s3[k]:
                second = f(i, j + 1, k + 1)

            return first or second

        if len(s1) + len(s2) != len(s3):
            return False

        return f(0, 0, 0)
