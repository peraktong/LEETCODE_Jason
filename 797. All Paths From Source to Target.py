## use recursion
def allPathsSourceTarget(graph):
    N = len(graph)

    def solve(node):
        if node == N - 1:
            return [[N - 1]]
        else:
            ans = []
            for nei in graph[node]:

                for path in solve(nei):
                    ans.append([node] + path)


            return ans

    return solve(0)


# 0-1 0-2; 1-3,2-3
graph = [[1,2], [3], [3], []]

print(allPathsSourceTarget(graph=graph))