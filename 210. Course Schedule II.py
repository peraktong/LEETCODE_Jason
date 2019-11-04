import collections


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Like course schedule 2, use graph
        dic = collections.defaultdict(set)
        neighbor = collections.defaultdict(set)
        for p in prerequisites:
            dic[p[0]].add(p[1])
            neighbor[p[1]].add(p[0])
        # include ones without prerequisites first, take them first
        stack = [i for i in range(numCourses) if not dic[i]]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node)
            for i in neighbor[node]:
                # This means node is taken and we do not need to consider the prerequisites for it
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return ans if not dic else []

"""
# can also do BFS: 
import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        dic = {i: set() for i in xrange(numCourses)}
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        # queue stores the courses which have no prerequisites
        queue = collections.deque([i for i in dic if not dic[i]])
        count, res = 0, []
        while queue:
            node = queue.popleft()
            res.append(node)
            count += 1
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    queue.append(i)
        return res if count == numCourses else []
            
        
        

"""
