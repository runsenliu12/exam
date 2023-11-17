class Solution:
    def partition(self, s: str):
        def is_palindrome(string):
            return string == string[::-1]  # 判断字符串是否为回文串的函数

        def backtrack(start, path):
            if start == len(s):  # 如果当前起始位置已经遍历到字符串末尾，将当前路径加入结果集合
                partitions.append(path[:])
                return

            for end in range(start + 1, len(s) + 1):  # 从当前起始位置向后遍历字符串
                substring = s[start:end]  # 获取当前子串
                if is_palindrome(substring):  # 如果当前子串是回文串，继续向后回溯
                    path.append(substring)  # 将当前回文子串加入路径
                    backtrack(end, path)  # 继续向后回溯
                    path.pop()  # 回溯到上一层，移除当前子串，尝试其他可能性

        partitions = []  # 存储所有可能的分割方案
        backtrack(0, [])  # 开始回溯，起始位置从0开始
        return partitions  # 返回所有的分割方案


if __name__ == "__main__":
    s = Solution()
    print(s.partition(s="aabccc"))
