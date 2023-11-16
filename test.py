from itertools import permutations

print(list(permutations(["foo", "bar"], len(["foo", "bar"]))))


from collections import defaultdict
from math import gcd

from collections import defaultdict


def maxPoints(points):
    if len(points) <= 2:
        return len(points)

    max_points = 0

    for i in range(len(points)):
        slopes = defaultdict(int)
        same_points = 1  # 记录和当前点重合的其他点数
        for j in range(i + 1, len(points)):
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]

            if dx == 0 and dy == 0:
                same_points += 1
                continue

            # 计算最大公约数，确保斜率存储的精确性
            gcd1 = gcd(dx, dy)
            slope = (dx // gcd1, dy // gcd1)
            slopes[slope] += 1

        current_max = same_points
        for slope_count in slopes.values():
            current_max = max(current_max, slope_count + same_points)

        max_points = max(max_points, current_max)

    return max_points


def get_gcd(a, b):
    if b == 0:
        return a
    return get_gcd(b, a % b)


# 示例
points1 = [[1, 1], [2, 2], [3, 3]]
points2 = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
print(maxPoints(points1))  # 输出：3
print(maxPoints(points2))  # 输出：4
