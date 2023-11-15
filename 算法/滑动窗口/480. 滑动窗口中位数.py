from typing import List


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = sorted(nums[:k])

        def get_median(window):
            if k % 2 == 0:
                return (window[k // 2 - 1] + window[k // 2]) / 2
            else:
                return window[k // 2]

        for i in range(k, len(nums)):
            result.append(get_median(window))

            # 移除窗口最左边的元素，并插入新元素的正确位置
            window.remove(nums[i - k])
            j = 0
            while j < len(window) and nums[i] > window[j]:
                j += 1
            window.insert(j, nums[i])

        # 处理最后一个窗口的中位数
        result.append(get_median(window))

        return result
