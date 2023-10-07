"""

给定一个正整数 n ，将其拆分为 k 个 正整数 的和（ k >= 2 ），并使这些整数的乘积最大化。

返回 你可以获得的最大乘积 。



示例 1:

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例 2:

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。

`dp` 的状态转移公式如下：

对于整数 `i`，我们需要遍历 `j` 从 `1` 到 `i - 1`，计算 `dp[i]` 的值。`dp[i]` 的状态转移公式为：

```plaintext
dp[i] = max(dp[i], j * dp[i - j], j * (i - j))
```

这个公式的含义是，我们可以选择以下三种方式来计算 `dp[i]`：

1. 不拆分 `i`，即 `dp[i] = i`。

2. 将 `i` 拆分成两部分 `j` 和 `(i - j)`，并使用 `dp[i - j]` 来计算 `(i - j)` 的最大乘积，然后乘以 `j`，即 `j * dp[i - j]`。

3. 与第二种方式类似，将 `i` 拆分成两部分 `j` 和 `(i - j)`，但是这次不使用 `dp[i - j]`，而是直接计算 `(i - j)` 的值乘以 `j`，即 `j * (i - j)`。

然后，我们比较这三种方式的结果，取其中的最大值作为 `dp[i]` 的值，以确保得到整数 `i` 拆分后的最大乘积。这样就可以逐步计算出 `dp[n]`，其中 `n` 是给定的整数。
"""


class Solution:
    def integerBreak(self, n: int) -> int:
        # dp[i] = max(dp[i], j * (i-j) , j * dp[i-i])
        dp = [0] * (n + 1)
        dp[2] = 1
        for i in range(3, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])

        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.integerBreak(10))
