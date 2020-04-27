'''
Problem Statement ->
            Given two strings text1 and text2, return the length 
            of their longest common subsequence.

            A subsequence of a string is a new string generated 
            from the original string with some characters(can be none) 
            deleted without changing the relative order of the remaining 
            characters. (eg, "ace" is a subsequence of "abcde" while "aec" 
            is not). A common subsequence of two strings is a subsequence 
            that is common to both strings.

            If there is no common subsequence, return 0.

Example ->
            Input: text1 = "abcde", text2 = "ace" 
            Output: 3  
            Explanation: The longest common subsequence is "ace" and its length is 3.
'''

#Solution Using Dynamic Programming : Time O(n*m) Space O(n*m)


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = []
        for i in range(len(text2)+1):
            temp = [0]*(len(text1)+1)
            dp.append(temp)
        
        used = set()
        for i in range(1,len(text2)+1):
            for j in range(1,len(text1)+1):
                if text2[i-1] == text1[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                    
        return dp[-1][-1]
            
        
        