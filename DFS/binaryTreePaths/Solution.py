class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        allPathList = []
        if root.left:
            for i in self.binaryTreePaths(root.left):
                allPathList.append(str(root.val) + "->" + i)
        if root.right:
            for i in self.binaryTreePaths(root.right):
                allPathList.append(str(root.val) + "->" + i)
        return allPathList