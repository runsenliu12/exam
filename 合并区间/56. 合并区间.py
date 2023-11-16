class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        # 按照区间起始位置排序
        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            previous_interval = merged[-1]

            # 检查当前区间与前一个合并后的区间是否重叠
            if current_interval[0] <= previous_interval[1]:
                # 合并区间
                merged[-1][1] = max(current_interval[1], previous_interval[1])
            else:
                # 不重叠，加入合并列表
                merged.append(current_interval)

        return merged
