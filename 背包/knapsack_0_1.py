def knapsack_0_1(items, capacity):
    """
    解决0-1背包问题
    :param items: 物品列表，每个元素为元组(weight, value)，weight表示物品重量，value表示物品价值
    :param capacity: 背包容量
    :return: 背包能够获得的最大价值
    """
    n = len(items)  # 物品数量
    dp = [
        [0 for _ in range(capacity + 1)] for _ in range(n + 1)
    ]  # 创建动态规划数组，dp[i][j]表示前i个物品在背包容量为j时的最大价值

    for i in range(1, n + 1):  # 遍历物品
        weight, value = items[i - 1]  # 获取当前物品的重量和价值
        for j in range(1, capacity + 1):  # 遍历背包容量
            if j >= weight:  # 当前背包容量可以放下当前物品
                # 选择放入当前物品或不放入当前物品的最大价值
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:  # 当前背包容量放不下当前物品
                dp[i][j] = dp[i - 1][j]  # 不放入当前物品

    return dp[n][capacity]  # 返回背包能够获得的最大价值


# 示例调用
items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # 每个物品的重量和价值
capacity = 8  # 背包容量
max_value = knapsack_0_1(items, capacity)
print("背包能获得的最大价值为:", max_value)
