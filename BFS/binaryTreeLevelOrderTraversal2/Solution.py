# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        valueListPerLayer = []
        curLevelNodeList = [root]
        while curLevelNodeList:
            nextLevelNodeList = []
            curLevelValueList = []
            for node in curLevelNodeList:
                curLevelValueList.append(node.val)
                if node.left:
                    nextLevelNodeList.append(node.left)
                if node.right:
                    nextLevelNodeList.append(node.right)
            valueListPerLayer.append(curLevelValueList)
            curLevelNodeList = nextLevelNodeList
        return valueListPerLayer[::-1]
