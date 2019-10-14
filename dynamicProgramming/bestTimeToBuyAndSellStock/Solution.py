class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxOutput = 0
        minValue = prices[0]
        for i in prices:
            maxOutput = max(maxOutput, i - minValue)
            minValue = min(minValue,  i)
        return maxOutput

if __name__ == '__main__':
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])
    print s.maxProfit([7,6,4,3,1])
