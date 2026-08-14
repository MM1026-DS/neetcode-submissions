# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root 
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr = curr.right 
            elif p.val<curr.val and q.val<curr.val:
                curr = curr.left 
            else:
                return curr 
# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         ## I will create dictionary and store the values values and nodes 

#         def dfs(root,node, track_parent_dict):
#             if not root:
#                 return track_parent_dict
            
#             if root.val>node.val:
#                 track_parent_dict[root.val] = root
                

#                 dfs(root.left,node,track_parent_dict)

#             elif root.val<node.val:
#                 track_parent_dict[root.val] = root
                

#                 dfs(root.right,node,track_parent_dict)

#             else:
#                 track_parent_dict[root.val] = root
            
#             return track_parent_dict 
        

#         p_dict = {}
#         q_dict = {}
       

#         parent_p_dict = dfs(root,p,p_dict)
#         parent_q_dict = dfs(root,q,q_dict)


#         ## first case 
#         # common lowest tree 

#         lowest_common_parent = list(set(parent_p_dict.keys()).intersection(set(parent_q_dict.keys())))
        



#         return parent_q_dict[self.lca(lowest_common_parent,list(parent_p_dict.keys()),list(parent_q_dict.keys()))] if len(lowest_common_parent)>0 else 'None'


#     def lca(self,common_parent,parent_p_list,parent_q_list):
#         ## it will give the distance 
#         ## common parent is array 
        

#         min_dist = float('inf')
#         reverse_parent_p_list = parent_p_list[::-1]
#         reverse_parent_q_list = parent_q_list[::-1]
#         lowest_common_parent = None
#         for parent in common_parent:

#             dist_p = reverse_parent_p_list.index(parent)
#             dist_q = reverse_parent_q_list.index(parent)
#             curr_min_dist = max(dist_p,dist_q)
#             if curr_min_dist<min_dist:
#                 min_dist = curr_min_dist 
#                 lowest_common_parent = parent
        
#         return lowest_common_parent

        