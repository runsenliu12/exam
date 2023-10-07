from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        if not nums:
            return result

        n = len(nums)

        # 使用列表作为双端队列来存储窗口内元素的索引
        window = []

        for i in range(n):
            # 移除窗口外的元素索引
            if window and window[0] < i - k + 1:
                window.pop(0)

            # 从队列右侧移除小于当前元素的元素索引
            while window and nums[window[-1]] < nums[i]:
                window.pop()

            # 将当前元素的索引添加到窗口
            window.append(i)

            # 当窗口完全覆盖k个元素时，将窗口的最大值添加到结果列表中
            if i >= k - 1:
                result.append(nums[window[0]])

        return result
