from . import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        if len(preorder) != len(inorder):
            return None
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        locate = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:locate+1], inorder[0:locate])
        root.right = self.buildTree(preorder[locate+1:], inorder[locate+1:])
        return root
