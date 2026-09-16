class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                x+=s[i].lower()
        print(x,x[::-1])
        if x== x[::-1]:
            return True
        else:
            return False
        