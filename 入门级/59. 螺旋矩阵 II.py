from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        num = 1

        while left <= right and top <= bottom:
            # 从左到右填充上边界
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1

            # 从上到下填充右边界
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1

            # 从右到左填充下边界
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

            # 从下到上填充左边界
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

        return matrix


if __name__ == "__main__":
    S = Solution()
    print(S.generateMatrix(4))
