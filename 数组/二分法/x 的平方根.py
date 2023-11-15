def sqrt_binary_search(x, epsilon=1e-6):
    if x < 0:
        return None  # 负数没有实数平方根
    if x == 0 or x == 1:
        return x

    left, right = 0, x
    while right - left > epsilon:
        mid = (left + right) / 2
        square = mid * mid
        if square == x:
            return mid
        elif square < x:
            left = mid
        else:
            right = mid

    return left

# 示例测试
number = 10  # 要计算平方根的数
sqrt_result = sqrt_binary_search(number)
print(f"平方根：{sqrt_result:.4f}")