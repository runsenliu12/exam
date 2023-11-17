"""


给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。



注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。


示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
示例 2：

输入：s = "a", t = "a"
输出："a"
解释：整个字符串 s 是最小覆盖子串。
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。


提示：

m == s.length
n == t.length
1 <= m, n <= 105
s 和 t 由英文字母组成
"""
from collections import Counter

from collections import Counter


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        target_count = Counter(t)  # 统计 t 中字符的出现次数
        required = len(target_count)  # t 中唯一字符的总数

        start = 0
        min_len = float("inf")
        result = ""
        window_count = {}

        formed = 0  # 记录窗口内已经匹配的字符数
        left = 0  # 窗口左指针

        for right in range(len(s)):
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1

            # 如果当前字符在 t 中且出现次数达到要求，则匹配字符数增加
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # 当匹配字符数等于 t 中唯一字符总数时，开始移动左指针缩小窗口
            while formed == required and left <= right:
                # 更新最小子串结果
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    result = s[left : right + 1]

                left_char = s[left]
                window_count[left_char] -= 1

                # 如果左指针指向的字符在 t 中且窗口内该字符数量不满足要求，则匹配字符数减少
                if (
                    left_char in target_count
                    and window_count[left_char] < target_count[left_char]
                ):
                    formed -= 1

                left += 1  # 移动左指针

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow(s="ADOBECODEBANC", t="ABC"))
