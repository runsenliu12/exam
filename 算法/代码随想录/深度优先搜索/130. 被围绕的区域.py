"""

给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。


示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
"""


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(i, j):
            if (
                i < 0
                or i >= len(board)
                or j < 0
                or j >= len(board[0])
                or board[i][j] != "O"
            ):
                return
            board[i][j] = "#"  # 将当前'O'标记为特殊字符'#'
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i, j + 1)

        if not board or not board[0]:
            return

        # 遍历四条边上的'O'，对每个 'O' 进行DFS
        for i in range(len(board)):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][-1] == "O":
                dfs(i, len(board[0]) - 1)
        for j in range(len(board[0])):
            if board[0][j] == "O":
                dfs(0, j)
            if board[-1][j] == "O":
                dfs(len(board) - 1, j)

        # 遍历整个矩阵，将剩余的'O'修改为'X'，同时将'#'恢复为'O'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
