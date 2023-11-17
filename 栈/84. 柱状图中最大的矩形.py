class Solution:
    def largestRectangleArea(self, heights):
        if not heights:
            return 0

        stack = []
        max_area = 0
        heights.append(0)  # 在末尾添加高度为0的柱子，确保所有柱子都能被处理到

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                # 遇到较小柱子时，计算以栈顶柱子高度为高的矩形面积
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area


if __name__ == "__main__":
    sol = Solution()

    # 测试案例 1
    heights1 = [2, 1, 5, 6, 2, 3]
    print(sol.largestRectangleArea(heights1))  # 应输出 10

    # 测试案例 2
    heights2 = [2, 4]
    print(sol.largestRectangleArea(heights2))  # 应输出 4

    # 测试案例 3
    heights3 = [1, 2, 3, 4, 5]
    print(sol.largestRectangleArea(heights3))  # 应输出 9

    # 测试案例 4
    heights4 = [5, 4, 3, 2, 1]
    print(sol.largestRectangleArea(heights4))  # 应输出 9

    # 测试案例 5
    heights5 = [2, 1, 2]
    print(sol.largestRectangleArea(heights5))  # 应输出 3


"""

这段代码实现了一个求解柱状图中能勾勒出的最大矩形面积的算法。它采用了单调栈的思想来解决这个问题。

### 思路：
1. **单调栈：** 使用栈来存储柱子的索引。栈中的柱子满足单调性，即递增或递减的性质。
2. **遍历柱子：** 遍历柱子高度数组。
3. **栈维持递增序列：** 如果当前柱子的高度小于栈顶柱子的高度，就弹出栈顶的柱子，并计算以弹出的柱子高度为高的矩形面积。此时的宽度为当前柱子索引与弹出柱子索引之差，即 `width = i - stack[-1] - 1`。
4. **更新最大面积：** 计算出面积后，取最大值更新最大面积值。
5. **继续遍历：** 将当前柱子的索引加入栈中，继续遍历下一个柱子。

整体思路是利用栈来维护一个递增的柱子索引序列，每当遇到一个较矮的柱子时，就计算以当前柱子高度为高的矩形面积，以此更新最大面积值。

这个算法的时间复杂度是 O(n)，其中 n 是柱子的数量。
"""
