class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.depth(root) != -1
    # -1 代表二叉树已经不平衡
    def depth(self, root):
        if not root:
            return 0
        leftTreeDepth = self.depth(root.left)
        if leftTreeDepth == -1:
            return -1
        rightTreeDepth = self.depth(root.right)
        if rightTreeDepth == -1:
            return -1
        return max(leftTreeDepth, rightTreeDepth) + 1 if abs(leftTreeDepth - rightTreeDepth) <= 1 else -1


    # normal way to solve the question
    # def isBalanced(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     if not root:
    #         return True
    #     if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(self.depth(root.left) - self.depth(root.right)) <= 1:
    #         return True
    #     else:
    #         return False
    #
    # def depth(self, root):
    #     if not root:
    #         return 0
    #     return max(self.depth(root.left), self.depth(root.right)) + 1