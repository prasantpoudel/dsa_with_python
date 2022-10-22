"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the first row and column to 1
        # Since the combination for 
        # dp[i][0] = dp[i-1][0]
        # dp[0][j] = dp[0][j-1]
        # dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # df_table = [[1]*n] + [[1] + [0]*(n-1) ] * (m-1)
		# Since dp[i][j] only depends on the calculated cells before,
		# we can simply initialize the value of all cells to 1.
        dp = [[1]*n] * m

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

        return dp[-1][-1]


