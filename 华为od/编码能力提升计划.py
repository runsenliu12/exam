from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        l, r = 0, sum(time)
        while l < r:
            mid = (l + r) >> 1
            if self.check(mid, time, m):
                r = mid
            else:
                l = mid + 1
        return l

    def check(self, limit, cost, day):
        use_day, total_time, max_time = 1, 0, cost[0]
        for i in cost[1:]:
            if total_time + min(max_time, i) <= limit:
                total_time, max_time = total_time + min(max_time, i), max(max_time, i)
            else:
                use_day += 1
                total_time, max_time = 0, i
        return use_day <= day


solution = Solution()

# 示例1
time1 = [1, 2, 2, 3, 5, 4, 6, 7, 8]
m1 = 5
result1 = solution.minTime(time1, m1)
print(result1)  # 输出 4

# 示例2
time2 = [999, 999, 999]
m2 = 4
result2 = solution.minTime(time2, m2)
print(result2)  # 输出 0
