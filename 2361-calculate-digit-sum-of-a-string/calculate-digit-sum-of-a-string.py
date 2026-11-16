class Solution:
    def digitSum(self, s: str, k: int) -> str:
        cop = s

        while len(cop) > k:
            new_str = ""
            i = 0

            while i < len(cop):
                cp = cop[i:i+k]
                a = 0

                for j in cp:
                    a += int(j)

                new_str += str(a)
                i += k

            cop = new_str

        return cop