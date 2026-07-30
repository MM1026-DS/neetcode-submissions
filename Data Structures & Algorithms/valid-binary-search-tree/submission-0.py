# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node,range_arr):
            if not node:
                return True 

          
            if range_arr[0]<node.val<range_arr[1]:
                leftrange = (range_arr[0],node.val)
                rightrange = (node.val,range_arr[1])
                l = dfs(node.left,leftrange)
                r = dfs(node.right,rightrange)
                return l and r 

            else:
                return False 
            
            
        
        
        range_arr = (float('-inf'),float('inf'))
        if dfs(root,range_arr):
            return True 
        return False
        
        
        

        