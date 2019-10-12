from TreeNode import TreeNode
class Solution(object):
    def listToTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        lenghth = len(nums)
        deep = 0  # 树深
        while lenghth != 0:
            deep += 1
            lenghth /= 2

        root = TreeNode(nums[0])  # 根节点，固定
        preLevelNodeList = [root]  # 上一层结点列表
        level = 2

        while level < deep:    # 从第二层开始遍历，迭代，直到倒数第二层，倒数第一层不满足等比数列的结点数量规律
            curLevelNodeValList = nums[2**(level-1)-1:2**(level)-1]   # 当前层结点值列表
            curLevelNodeList = list()  # 当前层结点列表，需要在 for 循环中生成
            index = 0
            for node in preLevelNodeList:
                if node:
                    node.left = TreeNode(curLevelNodeValList[index])
                    curLevelNodeList.append(node.left)
                    index += 1
                    node.right = TreeNode(curLevelNodeValList[index])
                    curLevelNodeList.append(node.right)
                    index += 1
                else:
                    index += 2
            preLevelNodeList = curLevelNodeList
            level += 1

        lastLevelNodeValList = nums[2**(level-1)-1:len(nums)]   # 最后一层节点值，存在不满足规律的可能性，如第三层的结点数为 2，不为 4
        index = 0
        for node in preLevelNodeList:
            if node:
                if index < len(lastLevelNodeValList):
                    node.left = TreeNode(lastLevelNodeValList[index])
                    index += 1
                if index < len(lastLevelNodeValList):
                    node.right = TreeNode(lastLevelNodeValList[index])
                    index += 1
            else:
                index += 2
        return root

    def preOrder(self, tree):
        """
        :param tree: TreeNode
        :return: listbb
        """
        if not tree:
            return []
        orderList = list()
        orderList.append(tree.val)
        orderList += self.preOrder(tree.left)
        orderList += self.preOrder(tree.right)
        return orderList

    def midOrder(self, tree):
        """
        :param tree: TreeNode
        :return: list
        """
        if not tree:
            return []
        orderList = list()
        orderList += self.midOrder(tree.left)
        orderList.append(tree.val)
        orderList += self.midOrder(tree.right)
        return orderList

    def backOrder(self, tree):
        """
        :param tree: TreeNode
        :return: list
        """
        if not tree:
            return []
        orderList = list()
        orderList += self.backOrder(tree.left)
        orderList += self.backOrder(tree.right)
        orderList.append(tree.val)
        return orderList


if __name__ == '__main__':
    s = Solution()
    list1 = [3, 9, 20, None, None, 15, 7]
    list2 = [1, 2, 2, 3, 3, None, None, 4, 4]
    root = s.listToTree(list2)

    print s.preOrder(root)
    print s.midOrder(root)
    print s.backOrder(root)

