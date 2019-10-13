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
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        root = self.generateTree(employees)
        idNode = self.findNode(root, id)
        if idNode:
            return self.curCalculateImportance(idNode)
        return 0

    def generateTree(self, employees):
        if not employees:
            return None
        nodeList = list()
        for i in employees:
            nodeList.append(Employee(i[0], i[1], i[2]))
        for node in nodeList:
            subNodeList = []
            for j in node.subordinates:
                subNodeList.append(nodeList[j-1])
            node.subordinates = subNodeList
        return nodeList[0]

    def findNode(self, employees, id):
        if not employees:
            return None
        if employees.id == id:
            return employees
        for node in employees.subordinates:
            if self.findNode(node):
                return node
        return None

    def curCalculateImportance(self, idNode):
        if not idNode:
            return 0
        importance = idNode.importance
        for node in idNode.subordinates:
            importance += self.curCalculateImportance(node)
        return importance

if __name__ == '__main__':
    s = Solution()
    print s.getImportance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1)
