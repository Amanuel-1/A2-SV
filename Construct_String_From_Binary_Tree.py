from typing import Optional

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans = ""
        
        def search(node):
            nonlocal ans
            if not node:
                return
            
            ans += str(node.val)
            
            if node.left:
                ans+="("
                search(node.left)
                ans+=")"
            if node.right:
                ans+="("
                search(node.right)
                ans+=")"
                
                
        search(root)
        return ans
