# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.allLeafValue(root1) == self.allLeafValue(root2)

    def allLeafValue(self, root):
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        leafList = []
        if root.left:
            leafList += self.allLeafValue(root.left)
        if root.right:
            leafList += self.allLeafValue(root.right)
        return leafList