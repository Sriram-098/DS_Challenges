class Solution:
    def isPalindrome(self, s: str) -> bool:
        x=""
        for i in range(len(s)):
            if s[i].isalnum():
                x+=s[i].lower()
        print(x)
        i=0
        j=len(x)-1
        while(i<=j):
            if(x[i]!=x[j]):
                return False
            i+=1
            j-=1
        return True

        