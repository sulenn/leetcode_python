# from . import TreeNode
from TreeNode import TreeNode
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        level = 2
        curLevelList = [root.left, root.right]
        while len(curLevelList) != 0:
            for j in range(2**(level-1)/2):
                if curLevelList[j].val != curLevelList[2**(level-1)-j-1].val:
                    return False
            nextLevelList = []
            for i in range(2**(level-1)):
                if curLevelList[i] is not None:
                    nextLevelList += [curLevelList[i].left]
                    nextLevelList += [curLevelList[i].right]
            curLevelList = nextLevelList
        return True

if __name__ == '__main__':
    n = TreeNode(1)
    n.left = TreeNode(2)
    n.right = TreeNode(2)
    n.left.left = TreeNode(3)
    n.left.right = TreeNode(4)
    n.right.left = TreeNode(4)
    n.right.right = TreeNode(3)
    s = Solution()
    print s.isSymmetric(n)
