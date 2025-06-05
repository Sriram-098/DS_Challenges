class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digits_to_letters={
            '2':"abc",
            "3":"def",
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        def f(i,com):
            if i==len(digits):
                ans.append(com[:])
                return 

            for letter in digits_to_letters[digits[i]]:
                f(i+1,com+letter)

        ans=[]
        f(0,"")
        return ans