# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum =0

        def search(node,num):
            nonlocal total_sum
            if not node:
                return
            if not (node.left or node.right):
                total_sum+= int(num+str(node.val))
            else:

                print(num+str(node.val))
                search(node.left,num+str(node.val))
                search(node.right,num+ str(node.val))
        
        search(root,"")

        return total_sum
        
