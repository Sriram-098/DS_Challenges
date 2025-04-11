class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        
        ans=0
        while(low<=high):
            if len(str(low))%2==0:
                x=str(low)
                st=x[:len(x)//2]
                end=x[len(x)//2:]

                sum_st=0
                for i in st:
                    sum_st+=int(i)

                sum_end=0
                for i in end:
                    sum_end+=int(i)

                if sum_st==sum_end:
                    print(low)
                    ans+=1

            low+=1
        return ans

                



        