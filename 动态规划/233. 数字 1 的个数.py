"""

给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。



示例 1：

输入：n = 13
输出：6
示例 2：

输入：n = 0
输出：0


提示：

0 <= n <= 109

这种方法的思路是通过迭代计算每个数位上数字 1 出现的次数，从低位到高位逐步累加得到总的数字 1 的个数。具体步骤如下：

1. 从个位开始，逐个计算每个数位上数字 1 出现的次数。
2. 使用 `low`、`cur` 和 `high` 表示当前处理的位数及其左右的数字值。
   - `low` 表示当前位数的低位数字的总和。
   - `cur` 表示当前位数的数字值。
   - `high` 表示当前位数的高位数字的值。
3. 在迭代过程中，分三种情况统计当前位数上数字 1 出现的次数：
   - 如果 `cur == 0`，说明当前位为 0，数字 1 出现次数取决于高位数字 `high` 的值。
   - 如果 `cur == 1`，当前位为 1，数字 1 出现次数由高位数字 `high` 和低位数字 `low` 决定。
   - 如果 `cur > 1`，当前位大于 1，数字 1 出现次数也由高位数字 `high` 决定。
4. 更新 `low`、`cur` 和 `high`，并迭代至下一个高位数字，直至所有数位处理完毕。

通过这种逐位迭代的方式，将每个数位上数字 1 的出现次数计算并累加，最终得到总的数字 1 的个数。
"""


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        count = 0
        digit = 1
        high = n // 10
        cur = n % 10
        low = 0

        while high != 0 or cur != 0:
            if cur == 0:
                count += high * digit
            elif cur == 1:
                count += high * digit + low + 1
            else:
                count += (high + 1) * digit

            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10

        return count
