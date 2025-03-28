from heapq import heappop, heappush
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        queries_with_indices = sorted(enumerate(queries), key=lambda x: x[1])
        ans = [0] * len(queries)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True

        count = 0

        for query_idx, query_val in queries_with_indices:
            while min_heap and min_heap[0][0] < query_val:
                val, r, c = heappop(min_heap)
                count += 1

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heappush(min_heap, (grid[nr][nc], nr, nc))

            ans[query_idx] = count

        return ans
