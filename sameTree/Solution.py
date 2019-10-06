class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if p is not None and q is not None and p.val == q.val:
            # left = self.isSameTree(p.left, q.left)
            # right = self.isSameTree(p.right, q.right)
            # return left and right
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
