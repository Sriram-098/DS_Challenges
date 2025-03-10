class Solution:
    def maxVowels(self, word: str, k: int) -> int:
        l=0
        r=0
        maxi=0
        count=0
        while(r<len(word)):
            if word[r] in "aeiou":
                count+=1
            while((r-l+1)>k):
                if word[l] in "aeiou":
                    count-=1
                l+=1
      


            maxi=max(maxi,count)
            r+=1
        return maxi
        