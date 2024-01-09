# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves = []
        
        def search(node):
            nonlocal leaves
            if not node:
                return
            else:
                if not node.left and not node.right:
                    leaves.append(node.val)
                if node.left:
                    search(node.left)
                if node.right:
                    search(node.right)
                    
        
        search(root1)
        lv1 = leaves
        leaves = []
        search(root2)

        return leaves == lv1