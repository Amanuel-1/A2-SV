"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        mx =0

        def explore(node,depth):
            nonlocal mx
            mx  = max(mx,depth)
            if not node:
                return
            elif not node.children:
                return
            else:
                for c in node.children:
                    explore(c,depth+1)
        if not root :
            return 0
        
        explore(root,1)

        return mx
                



        
