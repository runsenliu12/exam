"""
当解决这个问题时，可以按照以下步骤进行：

1. **构建高度数组**：
   - 遍历矩阵的每一行，对于每一列，从当前行向上数连续的1的数量，形成一个高度数组。这个数组记录了每一列连续1的高度。
   - 这样就构成了一个以当前行为底边的直方图。

2. **针对每一行计算最大矩形**：
   - 使用单调栈来计算直方图的最大矩形面积。
   - 遍历高度数组，在每一列确定的高度时，利用单调递增栈的思路，当当前高度小于栈顶元素时，开始弹栈计算面积。

3. **更新最大面积**：
   - 每次计算矩形面积时，更新最大面积值。

4. **返回最大面积**：
   - 返回得到的最大矩形面积值。

这个算法通过构建高度数组，并在每一行中利用单调栈的方式计算最大矩形面积，以达到找到二维矩阵中只包含1的最大矩形的目的。


"""


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix or not matrix[0]:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])
        heights = [0] * (cols + 1)  # 高度数组多出一位用于处理最后一个元素

        max_area = 0

        for i in range(rows):
            # 更新每行的连续高度
            for j in range(cols):
                if matrix[i][j] == "1":
                    heights[j] += 1
                else:
                    heights[j] = 0

            # 使用单调栈计算最大矩形面积
            stack = [-1]  # 栈底哨兵
            for k in range(cols + 1):
                while heights[k] < heights[stack[-1]]:
                    # 计算当前高度形成的矩形面积
                    h = heights[stack.pop()]
                    w = k - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(k)

        return max_area


# 测试用例
solution = Solution()
matrix1 = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(solution.maximalRectangle(matrix1))  # Output: 6

matrix2 = [
    ["0", "1", "1", "0", "1"],
    ["1", "1", "0", "1", "0"],
    ["0", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "0", "0", "0"],
]
print(solution.maximalRectangle(matrix2))  # Output: 9
