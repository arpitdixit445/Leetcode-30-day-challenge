'''
Problem Statement ->
        Given an array of non-negative integers, you are initially positioned 
        at the first index of the array. Each element in the array represents 
        your maximum jump length at that position. Determine if you are able 
        to reach the last index.

Example ->
        Input: [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what. Its maximum
                     jump length is 0, which makes it impossible to reach the last 
                     index.   
'''

#Solution : Time O(n), Space O(1)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        reach = nums[0]
        maxreach = float("-inf")
        jump = 1
        for i in range(len(nums)):
            if i <= reach:
                maxreach = max(maxreach,i+nums[i])
            else:
                if maxreach <= reach:
                    return False
                reach = maxreach
                maxreach = i+nums[i]
                jump += 1
        
        return True