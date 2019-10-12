"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        maxDepth = self.maxDepth(root.children[0])
        for i in range(1, len(root.children)):
            maxDepth = max(maxDepth, self.maxDepth(root.children[i]))
        maxDepth += 1
        return maxDepth
