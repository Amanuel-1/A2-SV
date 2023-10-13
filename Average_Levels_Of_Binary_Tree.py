# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        dq = deque([root])
        cursum =0
        
        ans=[]
        while dq:
                    
            cur = dq.popleft()

            if cur.left:
                dq.append(cur.left)
                
            if cur.right:
                dq.append(cur.right)
                
            

            newdq =deque()
            sum_=0
            length  = len(dq)
            while dq:
                newcur = dq.popleft()
                sum_+=newcur.val
                
                if newcur.left:
                    newdq.append(newcur.left)
                   
                if newcur.right:
                    newdq.append(newcur.right)
            
            ans.append(sum_/length)
                    
            dq = newdq

        return ans

            
                
                





        
