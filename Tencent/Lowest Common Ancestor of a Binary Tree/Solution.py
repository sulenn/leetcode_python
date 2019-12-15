from . import *

class Solution:

    def __init__(self):
        self.result = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return False
        self.recursive(root, p, q)
        return self.result

    def recursive(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> bool:
        if not root:
            return False
        left = self.recursive(root.left,p,q)
        right = self.recursive(root.right,p,q)
        mid = p == root or q == root
        if (left and right) or (left and mid) or (mid and right):
            self.result = root
        # if (left and right) or (left and mid) or (mid and right):
        #     self.result = root
        if left + right + mid >= 2:
            self.result = root
        return mid or left or right
