'''
Problem Statement ->
            Return the root node of a binary search tree that 
            matches the given preorder traversal.

            (Recall that a binary search tree is a binary tree 
            where for every node, any descendant of node.left 
            has a value < node.val, and any descendant of node.
            right has a value > node.val.  Also recall that a 
            preorder traversal displays the value of the node 
            first, then traverses node.left, then traverses 
            node.right.)

Example ->
            Input: [8,5,1,7,10,12]
            Output: [8,5,10,1,7,null,12]
'''

#solution Using recursion : Time O(n*log(n)), Space O(n*log(n))



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not len(preorder):
            return
        inorder = sorted(preorder)
        return self.build(0,len(preorder)-1,inorder,preorder)
    
    def build(self,left,right,inorder,preorder):
        if left > right:
            return None
        dd = {}
        for i in range(left,right+1):
            dd[inorder[i]] = i
        index = None
        for j in preorder:
            if j in dd:
                index = dd[j]
                break
        current = None
        if inorder[index] is not None:
            current = TreeNode(inorder[index])
            current.left = self.build(left,index-1,inorder,preorder)
            current.right = self.build(index+1,right,inorder,preorder)
        return current
        