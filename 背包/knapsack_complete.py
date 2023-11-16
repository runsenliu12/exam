def knapsack_complete(items, capacity):
    """
    解决完全背包问题
    :param items: 物品列表，每个元素为元组(weight, value)，weight表示物品重量，value表示物品价值
    :param capacity: 背包容量
    :return: 背包能够获得的最大价值
    """
    n = len(items)  # 物品数量
    dp = [0] * (capacity + 1)  # 创建动态规划数组，dp[j]表示背包容量为j时的最大价值

    for i in range(n):  # 遍历物品
        weight, value = items[i]  # 获取当前物品的重量和价值
        for j in range(weight, capacity + 1):  # 遍历背包容量
            # 选择放入当前物品或不放入当前物品的最大价值
            dp[j] = max(dp[j], dp[j - weight] + value)

    return dp[capacity]  # 返回背包能够获得的最大价值


# 示例调用
items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # 每个物品的重量和价值
capacity = 8  # 背包容量
max_value = knapsack_complete(items, capacity)
print("背包能获得的最大价值为:", max_value)
