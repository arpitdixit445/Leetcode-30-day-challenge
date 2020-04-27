'''
Problem Statement ->
            Given a 2D binary matrix filled with 0's and 1's, 
            find the largest square containing only 1's and 
            return its area.

Example ->
            Input: 

                1 0 1 0 0
                1 0 1 1 1
                1 1 1 1 1
                1 0 0 1 0

            Output: 4
'''

#Solution Using Dynamic Programming : Time O(n*m) Spave O(n*m)


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        dp = []
        length = len(matrix)
        breadth = len(matrix[0])
        for i in range(length+1):
            temp = [0]*(breadth+1)
            dp.append(temp)
            
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i+1][j+1] = min(dp[i+1][j],dp[i][j],dp[i][j+1])+1
        
        res = 0
        for i in dp:
            res = max(res,max(i))
        return res*res