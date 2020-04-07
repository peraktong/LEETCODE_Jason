import collections


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # DFS:
        graph = collections.defaultdict(set)

        def helper(source, target):
            if source not in seen:
                seen.add(source)
                if source == target:
                    return True
                return any(helper(neighbor, target) for neighbor in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph and helper(u, v):
                return u, v
            graph[u].add(v)
            graph[v].add(u)


