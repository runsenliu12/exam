def knapsack_multiple(items, capacity):
    """
    解决多重背包问题
    :param items: 物品列表，每个元素为元组(weight, value, count)，weight表示物品重量，value表示物品价值，count表示物品数量
    :param capacity: 背包容量
    :return: 背包能够获得的最大价值
    """
    n = len(items)  # 物品数量
    dp = [0] * (capacity + 1)  # 创建动态规划数组，dp[j]表示背包容量为j时的最大价值

    for i in range(n):  # 遍历物品
        weight, value, count = items[i]  # 获取当前物品的重量、价值和数量
        k = 1  # 当前物品可选数量
        while k <= count:  # 遍历当前物品的所有可选数量
            for j in range(capacity, weight - 1, -1):  # 逆序遍历背包容量
                # 选择放入当前物品或不放入当前物品的最大价值
                dp[j] = max(dp[j], dp[j - weight] + value)
            count -= k  # 更新可选数量
            k *= 2  # 数量加倍

        if count > 0:  # 处理剩余物品数量
            for j in range(capacity, weight - 1, -1):  # 逆序遍历背包容量
                # 选择放入当前物品或不放入当前物品的最大价值
                dp[j] = max(dp[j], dp[j - weight] + value * count)

    return dp[capacity]  # 返回背包能够获得的最大价值


# 示例调用
items = [(2, 3, 2), (3, 4, 1), (4, 5, 3), (5, 6, 2)]  # 每个物品的重量、价值和数量
capacity = 8  # 背包容量
max_value = knapsack_multiple(items, capacity)
print("背包能获得的最大价值为:", max_value)
