# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        '''
        if root is None:
            return 0

        ans = 0
        stack = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                ans += node.val
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return ans
        ''' 
        if root is None:
            return 0
        
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        
        return(
            root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        )