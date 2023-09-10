
def find_last_occurrence_binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid]  < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            result = mid
            left = mid + 1
    return result

# 使用方式示例
arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
result = find_last_occurrence_binary_search(arr, target)

if result != -1:
    print(f"最后一个等于 {target} 的元素位于索引 {result}")
else:
    print(f"{target} 不在列表中")
