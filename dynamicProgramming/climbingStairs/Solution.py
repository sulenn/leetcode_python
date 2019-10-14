class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        step1 = 1
        step2 = 2
        for i in range(2, n):
            step2, step1 = step2 + step1, step2
        return step2

    # recursive methord will come over time limit
    # def climbStairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n == 1:
    #         return 1
    #     if n == 2:
    #         return 2
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(2)
    print s.climbStairs(3)
    print s.climbStairs(4)
    print s.climbStairs(38)