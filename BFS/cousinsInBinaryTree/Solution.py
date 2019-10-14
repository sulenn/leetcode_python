# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    # official answer
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root:
            return False
        valueDepth = {}
        valueParent = {}
        def dfs(root, parent = None):
            if not parent:
                valueDepth[root.val] = 0
            else:
                valueDepth[root.val] = 1 + valueDepth[parent.val]
            valueParent[root.val] = parent
            if root.left:
                dfs(root.left, root)
            if root.right:
                dfs(root.right, root)
        dfs(root)
        return valueDepth[x] == valueDepth[y] and valueParent[x] != valueParent[y]


    # method with traversal by layer
    # def isCousins(self, root, x, y):
    #     """
    #     :type root: TreeNode
    #     :type x: int
    #     :type y: int
    #     :rtype: bool
    #     """
    #     if not root:
    #         return False
    #     curLevelNodeList = [root]
    #     while curLevelNodeList:
    #         curLevelValueList = []
    #         nextLevelNodeList = []
    #         for node in curLevelNodeList:
    #             curLevelValueList.append(node.val)
    #             nodeChildrenValueList = []
    #             if node.left:
    #                 nextLevelNodeList.append(node.left)
    #                 nodeChildrenValueList.append(node.left.val)
    #             if node.right:
    #                 nextLevelNodeList.append(node.right)
    #                 nodeChildrenValueList.append(node.right.val)
    #             if x in nodeChildrenValueList and y in nodeChildrenValueList:  # determine if tow nodes have the same parent node
    #                 return False
    #         if x in curLevelValueList and y in curLevelValueList:
    #             return True
    #         curLevelNodeList = nextLevelNodeList
    #     return False


if __name__ == '__main__':
    print 6 in [1,2,3,4,5]