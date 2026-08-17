"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        mapping_dict = {}

        def dfs(node):
            if not node:
                return
            if node in mapping_dict:
                return mapping_dict[node]

            ## copy 
            oldnodeval = node.val 
            copy= Node(oldnodeval)
            mapping_dict[node] = copy 

            for neighbor in node.neighbors:
                copied_neighbors = dfs(neighbor)
                copy.neighbors.append(copied_neighbors)

            return copy 

        return dfs(node)
       

        
        

        
          


        