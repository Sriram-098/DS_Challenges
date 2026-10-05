class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s=set(nums)
        ans=0
        for num in s:
            length = 1

            if num - 1 not in s:
                while num + length in s:
                    length += 1

            ans = max(ans, length)
        return ans
    