from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []  # stack of (num, steps)
        maxi = 0

        for num in nums:
            step = 0
            while st and st[-1][0] <= num:
                step = max(step, st[-1][1])
                st.pop()
            if st:
                step += 1
            else:
                step = 0
            st.append((num, step))
            maxi = max(maxi, step)

        return maxi
