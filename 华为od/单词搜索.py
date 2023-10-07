class Solution:
    def exist(self, board, word):
        def dfs(row, col, index):
            # 如果索引已经达到单词的长度，表示已经找到了匹配的单词
            if index == len(word):
                return True

            # 检查边界条件，如果越界，返回False
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False

            # 如果当前字符是通配符 "*"，尝试匹配下一个字符
            if board[row][col] == "*":
                for char in word:
                    if dfs(row, col, index + 1):
                        return True
                return False

            # 如果当前字符不匹配，返回False
            if board[row][col] != word[index]:
                return False

            # 临时将当前字符标记为已访问
            temp = board[row][col]
            board[row][col] = "#"

            # 递归探索上、下、左、右四个方向
            found = (
                dfs(row - 1, col, index + 1)
                or dfs(row + 1, col, index + 1)
                or dfs(row, col - 1, index + 1)
                or dfs(row, col + 1, index + 1)
            )

            # 恢复当前字符为未访问状态
            board[row][col] = temp

            return found

        # 遍历网格中的每个字符，作为起始点尝试开始搜索
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False


# 创建一个示例网格，包含了 * 通配符
board = [
    ["A", "B", "C", "E", "*"],
    ["S", "*", "C", "*", "S"],
    ["A", "D", "E", "E", "*"],
]

# 创建一个示例单词，包含 * 通配符
word = "ABCEFE"

# 创建 Solution 实例
solution = Solution()

# 调用 exist 方法检查单词是否存在于网格中
result = solution.exist(board, word)

# 打印结果
print(result)  # 输出True
