class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        change5=0
        change10=0
        for i in range(len(bills)):
            if bills[i]==5:
                change5+=1
            elif bills[i]==10:
                change10+=1
                if change5>0:
                    change5-=1
                else:
                    return False
            else:
                if change10>0 and change5>0:
                    change5-=1
                    change10-=1
                elif change5>=3:
                    change5-=3
                else:
                    return False

        return True
        