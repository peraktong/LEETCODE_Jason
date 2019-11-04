"""

import collections
equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]


def dfs(start, end, path, paths):
    if start == end and start in G:
        paths[0] = path
        return
    if start in vis:
        return
    vis.add(start)
    for node in G[start]:
        dfs(node, end, path * W[start, node], paths)


G, W = collections.defaultdict(set), collections.defaultdict(float)
# Here G means the expression for m1/m2
# Assume V !=0
for (A, B), V in zip(equations, values):
    # Here G[A]|{B} means G[A] = what is related to A
    G[A], G[B] = G[A] | {B}, G[B] | {A}
    W[A, B], W[B, A] = V, 1.0 / V

res = []
for X, Y in queries:
    paths, vis = [-1.0], set()
    # What we want is the start at X and return at Y
    dfs(X, Y, 1.0, paths)
    # !! use a comma to convert
    res.append(paths[0])

print(res)



"""


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # DFS:

        G, W = collections.defaultdict(set), collections.defaultdict(float)
        for (A, B), V in zip(equations, values):
            G[A], G[B] = G[A] | {B}, G[B] | {A}
            W[A, B], W[B, A] = V, 1.0 / V

        ans = []
        for X, Y in queries:
            paths, visit = [-1], set()
            val = self.dfs(G, W, X, Y, 1.0, visit)
            ans.append(val)
        return ans

    def dfs(self, G, W, start, stop, path, visit):
        if start == stop and start in G:
            return path
        if start in visit:
            return -1.0
        # visit is a set
        visit.add(start)
        # root is node to stop
        for node in G[start]:
            val = self.dfs(G, W, node, stop, path * W[start, node], visit)
            if val != -1:
                return val
        return -1




