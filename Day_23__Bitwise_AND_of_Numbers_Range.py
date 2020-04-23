'''
Problem Statement ->
        Given a range [m, n] where 0 <= m <= n <= 2147483647, 
        return the bitwise AND of all numbers in this range, 
        inclusive.

Example ->
        Input: [5,7]
        Output: 4
'''

#Solution Using Shifting : Time O(1), Space(1)

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m < n:
            m = m>>1
            n = n>>1
            count += 1  
            
        return m << count

