def cbrt_binary_search(x, epsilon=1e-6):
    if x < 0:
        return None  # 负数没有实数立方根

    left, right = 0, x
    while right - left > epsilon:
        mid = (left + right) / 2
        cube = mid * mid * mid
        if cube == x:
            return mid
        elif cube < x:
            left = mid
        else:
            right = mid
    return  left

# 示例测试
number =  98   # 要计算立方根的数
cbrt_result = cbrt_binary_search(number)
print(f"立方根：{cbrt_result:.3f}")
