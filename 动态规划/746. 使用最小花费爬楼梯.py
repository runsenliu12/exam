from typing import List


def minCostClimbingStairs(cost: List[int]) -> int:
    n = len(cost)
    dp = [0, 0]
    # dp[i]的定义：到达第i台阶所花费的最少体力为dp[i]。
    ## dp[i] = min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    for i in range(2, n + 1):
        dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))
    return dp[-1]


if __name__ == "__main__":
    print(minCostClimbingStairs([10, 15, 20]))
    print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
