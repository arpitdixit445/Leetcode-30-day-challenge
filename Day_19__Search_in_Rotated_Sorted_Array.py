'''
Problem Statement ->
            Suppose an array sorted in ascending order is rotated 
            at some pivot unknown to you beforehand.

            (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

            You are given a target value to search. If found in
            the array return its index, otherwise return -1.

            You may assume no duplicate exists in the array.


Note ->
            Your algorithm's runtime complexity must be in the
            order of O(log n).

Example ->
            Input: nums = [4,5,6,7,0,1,2], target = 0
            Output: 4
'''

#Solution - Using Binary Search : Time O(log(n)), Space O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        left = 0
        right = len(nums)-1
        currmax = float("-inf")
        max_index = 0
        while left <= right:
            mid = left+(right-left)//2
            
            if nums[mid] > currmax:
                max_index = mid
                currmax = nums[mid]
            
            if mid+1 < len(nums) and nums[mid] < nums[mid+1] and nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
                
        print(currmax)
                
        if target >= nums[0]:
            return self.binarysearch(nums,target,0,max_index)
        else:
            return self.binarysearch(nums,target,max_index+1,len(nums)-1)
        
    
    def binarysearch(self,nums,target,left,right):
        
        while left <= right:
            mid = left+(right-left)//2
            if target > nums[mid]:
                left = mid +1
            elif target < nums[mid]:
                right = mid-1
            elif target == nums[mid]:
                return mid
        return -1