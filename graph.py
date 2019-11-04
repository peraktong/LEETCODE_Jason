# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# gragh, BFS, DFS:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

ans = dfs(graph, 'A') # {'D', 'E', 'C', 'F', 'B', 'A'}
print(ans)