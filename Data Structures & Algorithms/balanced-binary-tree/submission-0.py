# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            if node == None:
                return 0  # height of empty tree is 0
            
            left_height = check(node.left)
            right_height = check(node.right)
            
            # If any child is unbalanced or heights differ by > 1
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            
            return 1 + max(left_height, right_height)
        
        return check(root) != -1