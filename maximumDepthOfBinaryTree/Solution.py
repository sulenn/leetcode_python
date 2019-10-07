class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



        # if root is None:
        #     return 0
        # leftDepth = 0
        # rightDepth = 0
        # leftLen = self.maxDepth(root.left) + 1
        # rightLen = self.maxDepth(root.right) + 1
        # if leftLen > rightLen:
        #     return leftLen
        # else:
        #     return rightLen



        # if root is None:
        #     return 0
        # leftLen = 1
        # rightLen = 1
        # if root.left is not None:
        #     leftLen = self.maxDepth(root.left) + 1
        # if root.right is not None:
        #     rightLen = self.maxDepth(root.right) + 1
        # if leftLen > rightLen:
        #     return leftLen
        # else:
        #     return rightLen