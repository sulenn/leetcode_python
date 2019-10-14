from TreeNode import TreeNode
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        leftTree = self.sortedArrayToBST(nums[0:len(nums)/2])
        rightTree = self.sortedArrayToBST(nums[len(nums)/2+1:len(nums)])
        root = TreeNode(nums[len(nums)/2])
        root.left = leftTree
        root.right = rightTree
        return root

if __name__ == '__main__':
    s = Solution()
    s.sortedArrayToBST([-10, -3, 0, 5, 9])
    print 5/2
    array = list()
    print array[2:1]