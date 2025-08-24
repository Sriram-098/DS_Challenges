class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k==1:
            return True
        total = sum(nums)
        n = len(nums)
        if total%k!=0:
            return False
        nums.sort(reverse=True)
        average = total//k
        if nums[0]>average:
            return False
        
        visited = [False]*n
        def dfs(cur, begin, k):
            if k==0:
                return True
            if cur>average:
                return False
            elif cur==average:
                return dfs(0, 0, k-1)
            for i in range(begin, n):
                if i>begin and nums[i]==nums[i-1] and not visited[i-1]:
                    continue
                if not visited[i]:
                    visited[i] = True
                    if dfs(cur + nums[i], i+1, k):
                        return True
                    visited[i] = False
            return False
        
        return dfs(0, 0, k)