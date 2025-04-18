from collections import defaultdict

class Solution:
    def isPossible(self, nums):
        freq=Counter(nums)
        extend_last=Counter()

        for num in nums:
            if freq[num]==0:
                continue

            elif extend_last[num-1]>0:
                extend_last[num]+=1
                extend_last[num-1]-=1

            elif freq[num+1]>0 and freq[num+2]>0:
                freq[num+1]-=1
                freq[num+2]-=1

                extend_last[num+2]+=1

            else:
                return False
            
            freq[num]-=1

        return True



        