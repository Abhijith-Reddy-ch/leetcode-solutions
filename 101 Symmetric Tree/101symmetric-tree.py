# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False

        stack = [(root.left,root.right)]
        while stack:
            left_node,right_node = stack.pop()

            if left_node is None and right_node is None:
                continue

            if left_node is None or right_node is None:
                return False

            if left_node.val != right_node.val:
                return False

            stack.append((left_node.left, right_node.right))
            stack.append((left_node.right, right_node.left))
            
        return True