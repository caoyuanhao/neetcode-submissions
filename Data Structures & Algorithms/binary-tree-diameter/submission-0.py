# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def diameter(root):
            nonlocal d
            if not root:
                return 0
            left=diameter(root.left)
            right=diameter(root.right)
            d=max(d,left+right)
            return max(left,right)+1
        diameter(root)
        return d