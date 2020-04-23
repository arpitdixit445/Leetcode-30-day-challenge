'''
Problem Statement ->
        Given an array of integers and an integer k, you need 
        to find the total number of continuous subarrays whose 
        sum equals to k.

Example ->
        Input:nums = [1,1,1], k = 2
        Output: 2
'''

# Solution Using a Hash Table : Time O(n), Space O(n)

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return 0
        
        count = 0
        ss = {0:1}
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            if (tot - k) in ss:
                count +=ss[tot-k]
            if tot in ss:
                ss[tot] += 1
            else:
                ss[tot] = 1
            
        return count
        
        
            
