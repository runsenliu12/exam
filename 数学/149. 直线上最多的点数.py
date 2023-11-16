from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def slope(p1, p2):
            """计算两点间的斜率，返回斜率的分子和分母的最简形式。"""
            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]
            if dx == 0:  # 垂直线
                return "inf", 0
            if dy == 0:  # 水平线
                return 0, "inf"
            g = gcd(dy, dx)  # 最大公约数，用于简化分数
            return dy // g, dx // g

        n = len(points)
        if n <= 2:
            return n

        max_points = 0
        for i in range(n):
            lines = defaultdict(int)
            duplicate = 1  # 包括点本身
            cur_max = 0
            for j in range(n):
                if i != j:
                    if points[i] == points[j]:
                        duplicate += 1
                    else:
                        lines[slope(points[i], points[j])] += 1
                        cur_max = max(cur_max, lines[slope(points[i], points[j])])

            max_points = max(max_points, cur_max + duplicate)

        return max_points


# 示例
sol = Solution()
points1 = [[1, 1], [2, 2], [3, 3]]
points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
result1 = sol.maxPoints(points1)
result2 = sol.maxPoints(points2)

print(result1, result2)
