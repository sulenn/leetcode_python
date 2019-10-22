class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        minValue = maxValue = -1
        for i in prices:
            if minValue == -1:
                minValue = i
                maxValue = i
                continue
            if i >= maxValue:
                maxValue = i
            else:
                profit += maxValue - minValue
                maxValue = i
                minValue = i
        return profit if maxValue == minValue else profit+maxValue-minValue

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])
    print s.maxProfit([1,2,3,4,5])
    print s.maxProfit([7,6,4,3,1])
