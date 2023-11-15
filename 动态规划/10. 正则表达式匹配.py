class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 创建一个二维数组 dp，用于记录匹配结果
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        # 空字符串和空正则表达式是匹配的
        dp[0][0] = True

        # 处理正则表达式中的 '*'，考虑 '*' 匹配零个字符的情况
        for j in range(1, len(p) + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        # 动态规划递推
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == ".":
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    # 考虑 '*' 匹配零个、一个或多个字符的情况
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == ".")
                    )

        return dp[len(s)][len(p)]


# 示例
solution = Solution()
print(solution.isMatch("aa", "a"))  # 输出：false
print(solution.isMatch("aa", "a*"))  # 输出：true
print(solution.isMatch("ab", ".*"))  # 输出：true
