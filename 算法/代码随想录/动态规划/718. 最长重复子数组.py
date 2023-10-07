"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：

A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3, 2, 1] 。
提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100

"""
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxlen = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    maxlen = max(maxlen, dp[i][j])
        return maxlen


if __name__ == "__main__":
    s = Solution()
    print(s.findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))
