# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        valueList = self.inOrder(root)
        if not valueList:
            return None
        root, curRoot = TreeNode(valueList[0])
        for i in valueList[1:]:
            curRoot.right = TreeNode(i)
            curRoot = curRoot.right
        return root

    def inOrder(self, root):
        if not root:
            return []
        valueList = []
        valueList += self.inOrder(root.left)
        valueList.append(root.val)
        valueList += self.inOrder(root.right)
        return valueList