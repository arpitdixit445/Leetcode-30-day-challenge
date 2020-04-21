'''
Problem Statement ->
        A binary matrix means that all elements are 0 or 1. 
        For each individual row of the matrix, this row is 
        sorted in non-decreasing order.

        Given a row-sorted binary matrix binaryMatrix, return 
        leftmost column index(0-indexed) with at least a 1 in it. 
        If such index doesn't exist, return -1.

        You can't access the Binary Matrix directly.  
        You may only access the matrix using a 
        BinaryMatrix interface:

        *   BinaryMatrix.get(x, y) returns the element of the 
            matrix at index (x, y) (0-indexed).
        
        *   BinaryMatrix.dimensions() returns a list of 2 elements 
            [n, m], which means the matrix is n * m.

        Submissions making more than 1000 calls to BinaryMatrix.get() 
        will be judged Wrong Answer.  Also, any solutions that 
        attempt to circumvent the judge will result in 
        disqualification.

        For custom testing purposes you're given the binary matrix 
        mat as input in the following four examples. You will not 
        have access the binary matrix directly.

Example ->
        Input: mat = [[0,0],[1,1]]
        Output: 0
'''

#Solution - Using Binary Search : Time O(m*log(n)), Space O(1)


# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def binarysearch(row,left,right):
            while left <= right:
                mid = left+(right-left)//2
                curr = binaryMatrix.get(row,mid)
                if curr != 1:
                    left = mid+1
                elif mid != 0 and binaryMatrix.get(row,mid-1) == 1:
                    right = mid-1
                else:
                    return mid
            return -1
        
        
        x,y = binaryMatrix.dimensions()
        mini = float("inf")
        for i in range(x):
            res = binarysearch(i,0,y-1)
            if res != -1:
                mini = min(res,mini)
        if mini == float("inf"):
            return -1
        return mini