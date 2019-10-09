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
            for j in range(len(curLevelList)/2):
                if not curLevelList[j] and not curLevelList[len(curLevelList)-j-1]:
                    continue
                if not curLevelList[j] or not curLevelList[len(curLevelList)-j-1]:
                    return False
                if curLevelList[j].val != curLevelList[len(curLevelList)-j-1].val:
                    return False
            nextLevelList = []
            for i in range(len(curLevelList)):
                if curLevelList[i] is not None:
                    nextLevelList += [curLevelList[i].left]
                    nextLevelList += [curLevelList[i].right]
            curLevelList = nextLevelList
            level += 1
        return True

if __name__ == '__main__':
    n = TreeNode(1)
    # n.left = TreeNode(2)
    # n.right = TreeNode(2)
    # n.left.left = TreeNode(3)
    # n.left.right = TreeNode(4)
    # n.right.left = TreeNode(4)
    # n.right.right = TreeNode(3)
    n.left = TreeNode(2)
    n.right = TreeNode(2)
    n.left.right = TreeNode(3)
    n.right.left = TreeNode(3)
    s = Solution()
    print s.isSymmetric(n)
