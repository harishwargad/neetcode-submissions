# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # while p and q:
        #     p_leftNode = p.left
        #     p_rightNode = p.right
        
        #     q_leftNode = q.left
        #     q_rightNode = q.right

        #     if p_leftNode == q_leftNode and p_rightNode == q_rightNode:
        #         return True 
        # return False 

        if p.val == None and q.val == None:
            return True
        elif p.val != q.val :
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)