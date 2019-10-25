class Solution:
    def findMaxConsecutiveOnes(self, nums):
        num = 0
        maximum = 0
        for i in nums:
            if i == 1:
                num += 1
            else:
                maximum = max(maximum, num)
                num = 0
        return max(maximum, num)

if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1,1,0,1,1,1]))
