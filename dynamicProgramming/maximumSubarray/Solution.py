class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        maximum = nums[0]
        sum = nums[0]
        for i in nums[1:]:
            sum = max(i, i + sum)
            maximum = max(maximum, sum)
        return maximum

if __name__ == '__main__':
    s = Solution()
    print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])