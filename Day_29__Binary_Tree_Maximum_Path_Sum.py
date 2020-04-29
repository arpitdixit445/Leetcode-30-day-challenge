'''
Problem Statement ->
            Given a non-empty binary tree, find the maximum path sum.

            For this problem, a path is defined as any sequence of nodes 
            from some starting node to any node in the tree along the 
            parent-child connections. The path must contain at least 
            one node and does not need to go through the root.

Example ->
            Input: [-10,9,20,null,null,15,7]

                -10
                /  \
               9   20
                  /  \
                 15   7

            Output: 42
            path = [15,20,7]

'''

#Solution Using DFS : Time O(n), Space O(n)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        arr = []
        self.helper(root,arr)
        if len(arr) == 0:
            return -2147483648
        return max(arr)
    
    def helper(self, root, arr):
        if root is None:
            return 0
        
        left = self.helper(root.left,arr)
        right = self.helper(root.right,arr)
        topass = max(max(left,right)+root.val,root.val)
        toadd = max(left+right+root.val, topass)
        arr.append(toadd)
        return topass
        

