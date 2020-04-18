'''
Problem Statement ->
        Given a m x n grid filled with non-negative numbers,
        find a path from top left to bottom right which
        minimizes the sum of all numbers along its path.

Note -> You can only move either down or right at any point in time.

Example ->
    Input:
    [
    [1,3,1],
    [1,5,1],
    [4,2,1]
    ]
    Output: 7
    Explanation: Because the path 1→3→1→1→1 minimizes the sum.

'''

#Solution - Using Dynammic programming : Time O(m*n), space O(m*n)

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        
        dp = []
        s = len(grid[0])
        for i in range(len(grid)):
            dp.append([0]*s)
        
        for x in range(len(dp)):
            for y in range(len(dp[0])):
                if x == 0:
                    dp[x][y] = dp[x][y-1] + grid[x][y]
                elif y == 0:
                    dp[x][y] = dp[x-1][y] + grid[x][y]
                else:
                    dp[x][y] = min(dp[x-1][y],dp[x][y-1]) + grid[x][y]
                    
        return dp[-1][-1]