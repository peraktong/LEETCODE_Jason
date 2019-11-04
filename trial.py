class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS:
        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V

        res = []
        for X, Y in queries:
            paths, vis = [-1.0], set()
            r = self.dfs(G, W, X, Y, 1.0, vis)
            res.append(r)
        return res

    def dfs(self, G, W, start, end, path, vis):
        if start == end and start in G:
            return path
        if start in vis:
            return -1.0

        vis.add(start)
        for node in G[start]:
            r = self.dfs(G, W, node, end, path * W[start, node], vis)
            if r != -1:
                return r
        return -1.0

