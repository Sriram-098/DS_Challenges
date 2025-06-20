"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        q=deque()
        q.append((id))
        emp={emp.id:emp for emp in employees }
        ans=emp[id].importance
        while(len(q)>0):
            curr=q.popleft()
            for subor in emp[curr].subordinates:
                ans+=emp[subor].importance
                q.append(subor)
        return ans
        