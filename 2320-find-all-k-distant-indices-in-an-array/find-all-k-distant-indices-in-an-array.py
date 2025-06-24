class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if nums[i]==key:
                l.append(i)
        ans=[]
        for i in range(len(nums)):
            for j in range(len(l)):
                if abs(i-l[j])<=k:
                    ans.append(i)
                    break
        return ans

        