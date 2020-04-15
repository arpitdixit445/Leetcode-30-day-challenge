'''
Problem Statement ->
                Given an array nums of n integers where n > 1, return 
                an array output such that output[i] is equal to the
                product of all the elements of nums except nums[i].
                
Example ->
      Input:  [1,2,3,4]
      Output: [24,12,8,6]
      
Note -> Please solve it without division and in O(n).
'''

# Solution - Using Bottom Up Processing : Time O(n), Space O(n)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before = [0]*len(nums)
        before[0] = 1
        after = [0]*len(nums)
        after[-1] = 1
        
        for i in range(1,len(nums)):
            before[i] = before[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            after[i] = after[i+1]*nums[i+1]
        
        result = [0]*len(nums)
        for i in range(len(nums)):
            result[i] = before[i]*after[i]
        return result
