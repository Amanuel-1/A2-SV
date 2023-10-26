# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_  =0
        def search(node,parent=None,grand=None):
            nonlocal sum_
            if not node:
                return
            else:
                if grand and grand.val%2==0:
                    sum_ +=node.val
                if node.left:
                    search(node.left,node,parent)
                if node.right:
                    search(node.right,node,parent)
            
        search(root)
        return sum_

                
                    
        
