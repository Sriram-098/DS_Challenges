class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        ans = 0

        def dfs(i, j):
            visited.add((i, j))
            count = 1

            for x in range(m):
                if grid[x][j] == 1 and (x, j) not in visited:
                    count += dfs(x, j)

            for y in range(n):
                if grid[i][y] == 1 and (i, y) not in visited:
                    count += dfs(i, y)

            return count

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    count = dfs(i, j)

                    if count > 1:
                        ans += count

        return ans