class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preMax = 0
        curMax = 0
        for i in nums:
            curMax, preMax = max(preMax + i, curMax), curMax
        return curMax

if __name__ == '__main__':
    s = Solution()
    # print s.rob([1,2,3,1])
    # print s.rob([2,7,9,3,1])
    print s.rob([6,6,4,8,4,3,3,10])