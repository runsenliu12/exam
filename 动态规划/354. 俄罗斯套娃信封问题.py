"""

给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi] ，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 最多能有多少个 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

注意：不允许旋转信封。


示例 1：

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
示例 2：

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1


当解决这个问题时，可以考虑以下思路：

1. **排序信封：** 首先，将给定的信封按照宽度进行升序排列。如果宽度相同，则按照高度进行降序排列。这一步是为了确保在后续的过程中，相同宽度的信封按照高度降序排列，这样可以避免宽度相同的信封互相套娃。

2. **寻找最长递增子序列：** 排序后的信封按照高度组成了一个新的序列。问题转化为在这个序列中寻找最长的递增子序列。在这个子序列中，每个信封的高度都比前一个信封的高度大，但是宽度又不能重复使用，因为排过序了，相同宽度的信封按高度降序排列。

3. **动态规划：** 使用动态规划来解决最长递增子序列问题。遍历信封，对每个信封都比较其高度与之前信封的高度，如果大于之前的信封高度，则将以当前信封结尾的最长递增子序列长度更新为前面某个符合条件的子序列长度加一。

4. **返回结果：** 最后返回最长递增子序列的长度即为最多能够套娃的信封数量。

这种方法通过转换问题为最长递增子序列的问题，利用动态规划来解决，有效地找出了最多能够套娃的信封数量。
"""
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        n = len(envelopes)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)

        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # n = len(envelopes)
        # dp = [1] * n
        #
        # for i in range(1, n):
        #     for j in range(i):
        #         if envelopes[i][1] > envelopes[j][1]:
        #             dp[i] = max(dp[i], dp[j] + 1)
        #
        # print(envelopes)
        # return max(dp)


if __name__ == "__main__":
    s = Solution()
    print(s.maxEnvelopes(envelopes=[[5, 4], [6, 4], [6, 7], [2, 3]]))
    print(s.maxEnvelopes(envelopes=[[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]))
