# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        

            
        mx=float('inf') 
        mn=float('-inf')
        node=root
        def ivb(node,mx,mn):
            if not node:
                return True       
            if node.val<=mn or node.val>=mx:
                return False
            return ivb(node.left,node.val,mn) and ivb(node.right,mx,node.val)

        return ivb(node, mx, mn)