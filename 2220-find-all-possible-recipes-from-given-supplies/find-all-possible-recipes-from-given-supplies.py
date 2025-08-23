from collections import deque,defaultdict
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        indegree={r:0 for r in recipes}
        graph=defaultdict(list)
        for recipie,ingreds in zip(recipes,ingredients):
            indegree[recipie]=len(ingreds)
            for ing in ingreds:
                graph[ing].append(recipie)
        q=deque(supplies)
        ans=[]
        while q:
            item=q.popleft()
            for reci in graph[item]:
                indegree[reci]-=1
                if indegree[reci]==0:
                    ans.append(reci)
                    q.append(reci)
        return ans
        

        