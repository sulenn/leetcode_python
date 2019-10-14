from Employee import Employee
"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    # recursive way
    def getImportance(self, employees, id):
        """
        :type employees: Employee list
        :type id: int
        :rtype: int
        """
        nodeDic = {node.id: node for node in employees}
        def f(i):
            e = nodeDic[i]
            return e.importance + sum(map(f, e.subordinates))
        return f(id)


    # none recursive way
    # def getImportance(self, employees, id):
    #     """
    #     :type employees: Employee list
    #     :type id: int
    #     :rtype: int
    #     """
    #     nodeDic = {node.id: node for node in employees}
    #     realEmployee = nodeDic[id]
    #     if not realEmployee:
    #         return 0
    #     nodeList = [realEmployee]
    #     importance = 0
    #     while nodeList:
    #         node = nodeList.pop()
    #         importance += node.importance
    #         for i in node.subordinates:
    #             nodeList.append(nodeDic[i])
    #     return importance




