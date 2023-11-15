"""

给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。

 

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def help(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 : r]

        res = ""
        for i in range(len(s)):
            temp = help(s, i, i)
            if len(temp) > len(res):
                res = temp
            temp1 = help(s, i, i + 1)
            if len(temp1) > len(res):
                res = temp1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
