"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        # DFS:
        emps = {employee.id: employee for employee in employees}
        def dfs(id):
            subordinates_importance = sum([dfs(sub_id) for sub_id in emps[id].subordinates])
            return subordinates_importance + emps[id].importance
        return dfs(id)