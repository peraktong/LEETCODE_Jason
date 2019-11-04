class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # use DFS: consider this as a graph:
        graph = [[] for i in xrange(numCourses)]
        visit = [0 for i in xrange(numCourses)]
        # Here graph is the pointer to the index for each course
        for x, y in prerequisites:
            graph[x].append(y)

        # return False if there is a ring
        def dfs(i):
            # is being visited
            if visit[i] == -1:
                return False
            # has been visited: no ring contain v[i] or its successor
            if visit[i] == 1:
                return True
            # being visited
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            # visited:
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


