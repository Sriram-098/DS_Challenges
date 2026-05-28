class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        window = Counter()

        left = 0
        right = 0
        res = []

        while right < len(s):
            # add current character
            window[s[right]] += 1

            # maintain window size
            if right - left + 1 > len(p):
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                left += 1

            # check anagram
            if window == p_count:
                res.append(left)

            right += 1

        return res



        