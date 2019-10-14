class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        allLevelValueList = []
        curLevelNodeList = [root]
        while curLevelNodeList:
            nextLevelNodeList = []
            curLevelValueList = []
            for node in curLevelNodeList:
                curLevelValueList.append(node.val)
                if node.children:
                    nextLevelNodeList += node.children
            allLevelValueList.append(curLevelValueList)
            curLevelNodeList = nextLevelNodeList
        return allLevelValueList