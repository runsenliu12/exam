from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []

        result = []
        window = deque()

        for end in range(len(nums)):
            # 如果队列非空且当前窗口内最大值不在窗口范围内，则移除队列头部元素
            while window and window[0] < end - k + 1:
                window.popleft()

            # 窗口滑动时，弹出队尾元素，直到队列为空或者窗口内当前元素大于队尾元素
            while window and nums[window[-1]] < nums[end]:
                window.pop()

            window.append(end)  # 将当前索引加入窗口

            # 如果已经形成了满足窗口长度的窗口，记录窗口内的最大值
            if end >= k - 1:
                result.append(nums[window[0]])

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
