from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1 or dp[i - 1][0] == 0:
                dp[i][0] = 0
            else:
                dp[i][0] = 1

        for j in range(1, n):
            if obstacleGrid[0][j] == 1 or dp[0][j - 1] == 0:
                dp[0][j] = 0
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0], [1, 0]]))
    print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 1], [0, 0]]))
