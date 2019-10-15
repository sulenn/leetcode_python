class NumArray(object):

    # dp method : sum(i, j) = sum(j) - sum(i)
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.sumList = [0]
        for i in nums:
            self.sumList.append(self.sumList[-1] + i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if 0<=i<len(self.sumList)-1 and 0<=j<len(self.sumList)-1 and j>=i:
            return self.sumList[j+1] - self.sumList[i]

    # # violent cache
    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.sumDic = {}
    #     for i in range(len(nums)):
    #         sum = 0
    #         for j in range(i, len(nums)):
    #             sum += nums[j]
    #             self.sumDic[(i, j)] = sum
    #
    # def sumRange(self, i, j):
    #     """
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     return self.sumDic[(i, j)] if self.sumDic[(i, j)] else False

    # # violent method
    # def __init__(self, nums):
    #     """
    #     :type nums: List[int]
    #     """
    #     self.nums = nums
    #
    # def sumRange(self, i, j):
    #     """
    #     :type i: int
    #     :type j: int
    #     :rtype: int
    #     """
    #     if 0<=i<len(self.nums) and 0<=j<len(self.nums) and j >=i:
    #         return sum(self.nums[i:j+1])

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)