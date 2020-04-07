class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS

        visited = [0] * n
        data = {x: [] for x in range(n)}
        for i, j in edges:
            data[i].extend([j])
            data[j].extend([i])

        def dfs(i, data, visited):
            if visited[i]:
                return
            visited[i] = 1
            for x in data[i]:
                dfs(x, data, visited)

        ans = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, data, visited)
                ans += 1
        return ans



