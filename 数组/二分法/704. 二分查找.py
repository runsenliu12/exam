'''

给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

'''


def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + ((right - left) >> 1)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"目标 {target} 在数组中的索引为 {result}")
    else:
        print(f"目标 {target} 不在数组中")