# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low = float("-inf")
        high = float("inf")

        def check(root,low,high):
            if root is None:
                return True

            if low >= root.val or root.val >=high:
                return False

            left_check = check(root.left,low,root.val)
            right_check = check(root.right,root.val,high)
            return left_check and right_check

        return check(root,low,high)
        

        