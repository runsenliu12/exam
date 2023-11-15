def find_first_occurrence_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            res = mid
            right = mid - 1
    return res


# 使用方式示例
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = find_first_occurrence_binary_search(arr, target)

if result != -1:
    print(f"第一个等于 {target} 的元素位于索引 {result}")
else:
    print(f"{target} 不在列表中")
