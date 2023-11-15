def find_first_greater_equal_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            result = mid  # 找到目标，但继续向左搜索更早的位置
            right = mid - 1
        else:
            left = mid + 1

    return result

# 使用方式示例
arr = [1, 2, 2, 3, 4, 5, 5, 6]
target = 3
result = find_first_greater_equal_binary_search(arr, target)

if result != -1:
    print(f"第一个大于等于 {target} 的元素位于索引 {result}")
else:
    print(f"没有大于等于 {target} 的元素")
