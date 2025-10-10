class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        def issingle(n):
            ans=0
            while n>0:
                rem=n%10
                rem=rem*rem
                ans=ans+rem
                n=n//10
            return ans
        slow=n
        fast=n
    
        
        while True:
            
            slow=issingle(slow)
            fast=issingle(issingle(fast))
            if slow==1 or fast==1:
                return True
            if slow==fast:
                return False
        return False
            
      
        