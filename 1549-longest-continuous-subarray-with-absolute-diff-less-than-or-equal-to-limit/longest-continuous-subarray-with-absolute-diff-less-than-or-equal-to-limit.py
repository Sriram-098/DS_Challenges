class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=0
        r=0
        mini=1e9
        maxi=-1e9
        ans=0
        maxq=deque()
        minq=deque()
        while(r<len(nums)):
            while maxq and nums[maxq[-1]]<=nums[r]:
                maxq.pop()
            maxq.append(r)
            while minq and nums[minq[-1]]>=nums[r]:
                minq.pop()
            minq.append(r)


            while maxq and minq and nums[maxq[0]]-nums[minq[0]]>limit:
                if minq[0]==l:
                    minq.popleft()
                if maxq[0]==l:
                    maxq.popleft()

                l+=1
                
            #print(ans,maxq,minq)
            ans=max(r-l+1,ans)
            
            r+=1
        return ans


        