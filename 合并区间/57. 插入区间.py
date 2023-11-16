from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        merged = []
        insert_pos = 0
        for interval in intervals:
            # 如果当前区间的结束小于新区间的开始，直接添加到merged
            if interval[1] < newInterval[0]:
                merged.append(interval)
                insert_pos += 1
            # 如果当前区间的开始大于新区间的结束，将新区间加入merged，并更新新区间
            elif interval[0] > newInterval[1]:
                merged.append(newInterval)
                newInterval = interval
            # 如果当前区间与新区间有重叠，合并区间
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        merged.append(newInterval)  # 添加最后一个新区间
        return merged


if __name__ == "__main__":
    # 测试用例
    test_cases = [
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        ([], [5, 7]),
        ([[1, 5]], [2, 3]),
        ([[1, 5]], [2, 7]),
        ([[1, 3], [6, 9]], [4, 5]),
        ([[1, 3], [6, 9]], [3, 6]),
        ([[3, 5], [6, 7], [8, 10], [12, 16]], [1, 2]),
        ([[1, 2], [3, 5], [6, 7], [8, 10]], [12, 20]),
        ([[1, 2], [2, 3], [3, 4], [4, 5]], [0, 6]),
    ]
    s = Solution()

    for intervals, new_interval in test_cases:
        result = s.insert(intervals, new_interval)
        print(
            f"Intervals: {intervals}, New Interval: {new_interval} -> Merged: {result}"
        )
