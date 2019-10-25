class Solution:

    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1
            nums[index] = - abs(nums[index])
        result = []
        for index, value in enumerate(nums):
            if value > 0:
                result.append(index+1)
        return result

    # my method
    # def findDisappearedNumbers(self, nums):
    #     if not nums:
    #         return []
    #     i = 0
    #     while i < len(nums):
    #         if nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
    #             temp = nums[i]
    #             nums[i] = nums[nums[i] - 1]
    #             nums[temp - 1] = temp
    #         else:
    #             i += 1
    #     result = []
    #     for index, value in enumerate(nums):
    #         if value != index + 1:
    #             result.append(index + 1)
    #     return result

if __name__ == '__main__':
    s = Solution()
    print(s.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
