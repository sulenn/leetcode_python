class Solution(object):
    # dp[i] = Math.min(dp[i - 1], dp[i - 2]) + cost[i];
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if not cost:
            return 0
        if len(cost) == 1:
            return cost[0]
        for i in range(2,len(cost)):
            cost[i] = min(cost[i-1], cost[i-2]) + cost[i]
        return min(cost[len(cost)-1], cost[len(cost)-2])