def find_last_less_equal_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    result = len(arr)

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            result = mid  # 找到目标，但继续向右搜索更晚的位置
            left = mid + 1
        else:
            right = mid - 1

    return result

# 使用方式示例
arr = [1,3,5,6]
target = 5
result = find_last_less_equal_binary_search(arr, target)

if result != -1:
    print(f"最后一个小于等于 {target} 的元素位于索引 {result}")
else:
    print(f"没有小于等于 {target} 的元素")
