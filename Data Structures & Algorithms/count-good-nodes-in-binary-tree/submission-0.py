# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,flag):
            if not node:
                return 0
            res=1 if node.val>=flag else 0
            flag=max(node.val,flag)
            res+=dfs(node.left,flag)
            res+=dfs(node.right,flag)
            return res
        return dfs(root,root.val)


            
